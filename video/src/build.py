# Monta o vídeo num único .html (fontes, fotos e logos embutidas).
import base64, pathlib
src = pathlib.Path(__file__).parent
root = src.parent.parent
b64 = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
rep = {
    'F_ALT3': b64(src/'fonts/alt300.woff2'), 'F_ALT4': b64(src/'fonts/alt400.woff2'),
    'F_MONT': b64(src/'fonts/mont.woff2'),
    'I_AURA': 'data:image/png;base64,' + b64(src/'aura.png'),
}
for k in ['sobre', 'cirurgia', 'consultorio', 'hero', 'clareamento', 'radiografia', 'prevencao']:
    rep['I_' + k.upper()] = 'data:image/webp;base64,' + b64(root/'assets/img'/f'{k}.webp')
html = (src/'apresentacao.template.html').read_text(encoding='utf8')
for k, v in rep.items():
    html = html.replace('{{' + k + '}}', v)
assert '{{' not in html, 'placeholder sobrando'
out = src.parent/'apresentacao-aura.html'
out.write_text(html, encoding='utf8')
print(out, round(out.stat().st_size / 1024), 'KB')
