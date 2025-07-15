# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pong.py'],
    pathex=[],
    binaries=[],
    datas=[('pong.png', '.'), ('pong_display.png', '.'), ('ponghit.wav', '.'), ('point_scored.mp3', '.'), ('powerup.mp3', '.'), ('win.mp3', '.'), ('button.mp3', '.'), ('russo.ttf', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
