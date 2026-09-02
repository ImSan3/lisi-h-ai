#!/usr/bin/env python3
"""一键更新模型数据：从 rapi.ycjg.top 拉取最新模型/检测平台，重建 index.html 内嵌数据，
并输出新旧模型对比 data/model-compare.json（供生成 XLSX 报告）。
用法：python3 update-models.py [--offline]  (--offline 只用 data/ 缓存，不发网络请求)
"""
import json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / 'index.html'
DATA = ROOT / 'data'
API = 'https://rapi.ycjg.top'
MODE_MAP = {'降重': 'reduce', '降ai': 'remove', '双降': 'both'}
LANG_MAP = {'ch': 'zh', 'en': 'en'}

# 站内展示名（prettyName 的唯一真源，JS 里同名映射需与此保持一致）
PRETTY = {
    'zh_jc_1_0325': '降重0325-1', 'zh_jc_2_0325': '降重0325-2',
    'zh_jc_3_0325': '降重0325-3', 'zh_jc_4_0325': '降重0325-4',
    'jc_muti_language_1': '超级改写(扩写降重+20%~40%)',
    'aigcmove_tp_s_merge_1': '混合模式',
    'aimove_weipu_0513': '维普专用0513',
    'aimove_weipu_0520': '格子达学校版专用0520',
    'gzd_0510': '格子达个人版0510',
    'wanfang_0731': '万方专用0731',
    'daya': '大雅专用0729',
    'paperpass0618': 'PaperPass专用0618',
    'aimove_matrix_s_1': '朱雀专用(小说新闻泛娱乐)',
    'aimove_大雅句子_1': '大雅/YY降AI力度强',
    'aimove_weipu_english': '英文降AI',
    'turnitin_s_1': 'Turnitin专用(质量高)',
    '5.09en': '英文双降',
    'aigcmove_wanfang_sj': '万方双降专用', 'aigcmove_weipu_sj': '维普双降专用',
    'aigcmove_daya_sj': '大雅双降专用', 'aigcmove_zhuque_sj': '朱雀双降专用',
    'aigcmove_paperpass_sj': 'PaperPass双降专用', 'aigcmove_turnitin_sj': '英语双降0826',
}
DESC30112 = {'1': '幅度小·学术性强', '2': '幅度小·学术性强', '3': '能力强·幅度中',
             '4': '能力强·幅度中', '5': '很强·幅度大'}


def pretty_name(code, name):
    if code in PRETTY:
        return PRETTY[code]
    m = re.match(r'^降重测试模式0325-(\d)$', name)
    if m:
        return f'降重0325-{m.group(1)}'
    m = re.match(r'^降ai模式-微度模式(\d)$', name)
    if m:
        return f'微度模式{m.group(1)}'
    m = re.match(r'^AI移除_260112_(\d)\s*\(', name)
    if m:
        return f'AI移除_{m.group(1)}({DESC30112.get(m.group(1), "")})'
    m = re.match(r'^(\d+)-(.+)$', name)  # 0731-万方专用 → 万方专用0731
    if m and not m.group(2).startswith(('zh_', 'en_')):
        return f'{m.group(2)}{m.group(1)}'
    return name


def get_json(url, cache):
    try:
        print(f'GET {url}')
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
        DATA.mkdir(exist_ok=True)
        (DATA / cache).write_text(json.dumps(d, ensure_ascii=False, indent=1))
        return d
    except Exception as e:
        print(f'  在线拉取失败({e})，使用缓存 {cache}')
        return json.loads((DATA / cache).read_text())


def build_model_data(ro):
    md = {}
    for mode_label, langs in ro['data'].items():
        mode = MODE_MAP[mode_label]
        md[mode] = {}
        for lang, platforms in langs.items():
            plats, models = [], {}
            for p in platforms:
                plats.append(p['name'])
                rec = (p.get('recommended_preset') or {}).get('code')
                models[p['name']] = [
                    {'code': x['code'], 'name': x['name'], 'recommended': x['code'] == rec}
                    for x in p.get('presets', [])
                ]
            md[mode][LANG_MAP[lang]] = {'platforms': plats, 'models': models}
    return md


def build_detect_data(dopt):
    out = {}
    for lang, arr in dopt['data']['platforms'].items():
        if lang in ('zh', 'en'):
            out[lang] = [{'task_platform': x['task_platform'],
                          'task_name': x['task_name'],
                          'price': x.get('price_per_1k_words')} for x in arr]
    return out


def old_model_data():
    """从 git HEAD 的 index.html 提取旧版 MODEL_DATA（JS 对象字面量，用 node 转成 JSON）"""
    src = subprocess.run(['git', '-C', str(ROOT), 'show', 'HEAD:index.html'],
                         capture_output=True, text=True).stdout
    m = re.search(r'const MODEL_DATA=(\{.*?\});\n', src, re.S)
    if not m:
        print('  未在 git HEAD 中找到旧 MODEL_DATA，跳过对比')
        return None
    js = json.dumps(m.group(1))
    r = subprocess.run(['node', '-e',
                        'console.log(JSON.stringify(eval("("+process.argv[1]+")"))) ', m.group(1)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print('  旧 MODEL_DATA 解析失败:', r.stderr[:300])
        return None
    return json.loads(r.stdout)


def compare(old, new, presets):
    """逐个模型对比：返回 Sheet1 行列表"""
    rows = []
    if not old:
        return rows
    strip = lambda n: n.replace(' ⭐推荐', '').strip()
    for mode in ('reduce', 'remove', 'both'):
        for lang in ('zh', 'en'):
            o, n = old.get(mode, {}).get(lang, {}), new[mode][lang]
            for p in n['platforms']:
                for m in n['models'].get(p, []):
                    old_list = o.get('models', {}).get(p, [])
                    hit = next((x for x in old_list if x['code'] == m['code']), None)
                    if hit is None and p not in o.get('platforms', []):
                        status, note = '平台新增', '该平台为本模式/语言新增'
                    elif hit is None:
                        status, note = '新增', '该平台此前无此模型'
                    else:
                        renamed = strip(hit['name']) != pretty_name(m['code'], m['name']) and \
                                  strip(hit['name']) != m['name']
                        status = '更名' if renamed else '保留'
                        note = f'旧名「{strip(hit["name"])}」' if renamed else ''
                    if m.get('recommended'):
                        note = (note + '；' if note else '') + 'API推荐位'
                    rows.append({'模式': mode, '语言': lang, '平台': p,
                                 '模型Code': m['code'], 'API名称': m['name'],
                                 '站内显示名': pretty_name(m['code'], m['name']),
                                 '旧名称': strip(hit['name']) if hit else '-',
                                 '状态': status, '备注': note})
            # 旧有新无 → 已下线
            for p in o.get('platforms', []):
                if p not in n['platforms']:
                    for x in o.get('models', {}).get(p, []):
                        rows.append({'模式': mode, '语言': lang, '平台': p,
                                     '模型Code': x['code'], 'API名称': '-',
                                     '站内显示名': '-', '旧名称': strip(x['name']),
                                     '状态': '平台下线', '备注': '新API此模式/语言已无该平台'})
                    continue
                for x in o.get('models', {}).get(p, []):
                    if not any(m['code'] == x['code'] for m in n['models'].get(p, [])):
                        rows.append({'模式': mode, '语言': lang, '平台': p,
                                     '模型Code': x['code'], 'API名称': '-',
                                     '站内显示名': '-', '旧名称': strip(x['name']),
                                     '状态': '已下线', '备注': '新API已移除该模型'})
    return rows


def main():
    offline = '--offline' in sys.argv
    if offline:
        ro = json.loads((DATA / 'rewrite-options.json').read_text())
        dopt = json.loads((DATA / 'detection-options.json').read_text())
        presets = json.loads((DATA / 'presets.json').read_text())
    else:
        ro = get_json(f'{API}/api/v2/rewrite-options', 'rewrite-options.json')
        dopt = get_json(f'{API}/api/v2/detection/options', 'detection-options.json')
        presets = get_json(f'{API}/api/v2/presets', 'presets.json')

    md = build_model_data(ro)
    dd = build_detect_data(dopt)

    # 一致性检查：rewrite-options 里用到的 preset 都应在 presets 总表中
    all_codes = {p['code'] for p in presets['presets']}
    used = {m['code'] for mode in md.values() for lang in mode.values()
            for ms in lang['models'].values() for m in ms}
    missing = used - all_codes
    print(f'模型总数(presets)={len(all_codes)}  站内用到={len(used)}  未收录={missing or "无"}')

    data_js = (f'let MODEL_DATA={json.dumps(md, ensure_ascii=False, separators=(",", ":"))};\n'
               f'let DETECT_DATA={json.dumps(dd, ensure_ascii=False, separators=(",", ":"))};')
    html = HTML.read_text()
    new_html, n = re.subn(
        r'(/\*__MODEL_DATA_START__\*/\n).*?(/\*__MODEL_DATA_END__\*/)',
        lambda m: m.group(1) + data_js + '\n' + m.group(2),
        html, flags=re.S)
    if n != 1:
        sys.exit('index.html 中未找到 MODEL_DATA 标记位（应恰好 1 处）')
    HTML.write_text(new_html)
    n_cfg = sum(len(l['platforms']) for mode in md.values() for l in mode.values())
    print(f'index.html 模型数据已重建：{n_cfg} 组模式/语言配置, '
          f'检测平台 zh={len(dd["zh"])} en={len(dd["en"])}')

    rows = compare(old_model_data(), md, presets)
    if rows:
        DATA.mkdir(exist_ok=True)
        (DATA / 'model-compare.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1))
        from collections import Counter
        print('逐个对比完成:', dict(Counter(r['状态'] for r in rows)))
        print('对比明细已写入 data/model-compare.json')


if __name__ == '__main__':
    main()
