import os
p='build.py'
s=open(p).read()
old='''            out.append(
                f'<figure class="fig"><a class="fig-link" href="{attr(src)}" data-zoom="1">'
                f'<img src="{attr(src)}" alt="{attr(alt)}" loading="lazy" decoding="async"></a>{cap_html}</figure>'
            )'''
new='''            svg_name = os.path.splitext(os.path.basename(src))[0] + ".svg"
            svg_path = os.path.join(ROOT, "figures", "svg", svg_name)
            redraw = ""
            if os.path.exists(svg_path):
                redraw = (
                    '<div class="fig-redraw"><img src="../assets/figures/svg/' + attr(svg_name) +
                    '" alt="' + attr(alt) + '（中文重绘）" loading="lazy" decoding="async"></div>'
                )
            out.append(
                f'<figure class="fig"><a class="fig-link" href="{attr(src)}" data-zoom="1">'
                f'<img src="{attr(src)}" alt="{attr(alt)}" loading="lazy" decoding="async"></a>{redraw}{cap_html}</figure>'
            )'''
if old not in s:
    raise SystemExit('figure block not found')
s=s.replace(old,new)
s=s.replace('''    fig_out = os.path.join(SITE, "assets", "figures")
    os.makedirs(fig_out, exist_ok=True)''','''    fig_out = os.path.join(SITE, "assets", "figures")
    os.makedirs(os.path.join(fig_out, "svg"), exist_ok=True)
    svg_src = os.path.join(ROOT, "figures", "svg")
    if os.path.isdir(svg_src):
        for name in os.listdir(svg_src):
            if name.endswith(".svg"):
                shutil.copy2(os.path.join(svg_src, name), os.path.join(fig_out, "svg", name))''')
open(p,'w').write(s)
print('build patched')
