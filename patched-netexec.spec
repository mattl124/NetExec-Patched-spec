# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Collect all SQLAlchemy submodules (fixes "No module named 'sqlalchemy.ext.declarative'")
sqlalchemy_hiddenimports = collect_submodules('sqlalchemy')
pypykatz_hiddenimports = collect_submodules('pypykatz')

a = Analysis(
    ['./nxc/netexec.py'],
    pathex=['./nxc'],
    binaries=[],
    datas=[
        ('./nxc/protocols', 'nxc/protocols'),
        ('./nxc/data', 'nxc/data'),
        ('./nxc/modules', 'nxc/modules')
    ],
    hiddenimports=[
        # Existing hidden imports
        'aardwolf',
        'aardwolf.connection',
        'aardwolf.commons.queuedata.constants',
        'aardwolf.commons.iosettings',
        'aardwolf.commons.target',
        'aardwolf.protocol.x224.constants',
        'certipy',
        'impacket.examples.secretsdump',
        'impacket.examples.regsecrets',
        'impacket.dcerpc.v5.lsat',
        'impacket.dcerpc.v5.transport',
        'impacket.dcerpc.v5.lsad',
        'impacket.dcerpc.v5.gkdi',
        'impacket.dcerpc.v5.rprn',
        'impacket.dcerpc.v5.even',
        'impacket.dcerpc.v5.even6',
        'impacket.dpapi_ng',
        'impacket.tds',
        'impacket.version',
        'impacket.ldap.ldap',
        'jwt',
        'nxc.connection',
        'nxc.protocols.smb.wmiexec',
        'nxc.protocols.smb.atexec',
        'nxc.protocols.smb.smbexec',
        'nxc.protocols.smb.mmcexec',
        'nxc.protocols.smb.smbspider',
        'nxc.protocols.smb.passpol',
        'nxc.protocols.mssql.mssqlexec',
        'nxc.parsers.ldap_results',
        'nxc.helpers.bash',
        'nxc.helpers.bloodhound',
        'nxc.helpers.even6_parser',
        'nxc.helpers.msada_guids',
        'nxc.helpers.ntlm_parser',
        'paramiko',
        'pefile',
        'pypsrp.client',
        'pylnk3',
        'pypykatz',
        'pyNfsClient',
        'masky',
        'msldap',
        'msldap.connection',
        'lsassy',
        'lsassy.dumper',
        'lsassy.parser',
        'lsassy.session',
        'lsassy.impacketfile',
        'bloodhound',
        'dns',
        'dns.name',
        'dns.resolver',
        'dploot',
        'dploot.triage',
        'dploot.triage.rdg',
        'dploot.triage.vaults',
        'dploot.triage.browser',
        'dploot.triage.credentials',
        'dploot.triage.masterkeys',
        'dploot.triage.mobaxterm',
        'dploot.triage.backupkey',
        'dploot.triage.wam',
        'dploot.triage.wifi',
        'dploot.triage.sccm',
        'dploot.lib.target',
        'dploot.lib.smb',
        'pyasn1_modules.rfc5652',
        'unicrypto.backends.pycryptodomex',
        'dateutil.relativedelta',
        'sspilib.raw._text',
        # Include all SQLAlchemy submodules
        *sqlalchemy_hiddenimports,
        # Include all pypykatz submodules
        *pypykatz_hiddenimports,
    ],
    hookspath=['./nxc/.hooks'],
    runtime_hooks=[],
    # exclude unnecessary DB drivers to silence warnings
    excludes=['pysqlite2', 'psycopg2', 'MySQLdb', 'rekall'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='nxc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon='./nxc/data/nxc.ico'
)
