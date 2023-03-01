import os

def chu():
#     libs = ["streamlit","adal","aiofiles","aiohttp","aiosignal","aiostream","altair","anyio",
#             "async-timeout","attrs","azure-cognitiveservices-search-imagesearch","azure-common",
#             "azure-core","beautifulsoup4","blinker","blobfile","bs4","cachetools","certifi",
#             "cffi","chardet","charset-normalizer","click","colorama","commonmark","corenlp-client",
#             "cryptography","cycler","decorator","discoart","docarray","docker","docker-pycreds",
#             "entrypoints","fastapi","filelock","flake8","fonttools","frozenlist","ftfy","gitdb",
#             "GitPython","google-api-core","google-api-python-client","google-auth",
#             "google-auth-httplib2","Google-Images-Search","googleapis-common-protos","grpcio",
#             "grpcio-health-checking","grpcio-reflection","guided-diffusion-sdk","h11","html5lib",
#             "httplib2","httptools","idna","importlib-metadata","isodate","jina","jina-hubble-sdk",
#             "Jinja2","joblib","jsonschema","kiwisolver","language-tool-python","lpips","lxml","lz4",
#             "MarkupSafe","matplotlib","mccabe","msrest","msrestazure","multidict","nltk","numpy",
#             "oauthlib","open-clip-torch","openai-clip","opencv-python","packaging","pandas","pathspec",
#             "pathtools","Pillow","pip","prometheus-client","promise","protobuf","psutil",
#             "py-bing-search","pyarrow","pyasn1","pyasn1-modules","pycodestyle","pycparser",
#             "pycryptodomex","pydantic","pydeck","pyfiglet","pyflakes","Pygments","PyJWT","Pympler",
#             "pyparsing","pyrsistent","PySocks","pyspellchecker","python-dateutil","python-dotenv",
#             "python-multipart","python-rake","python-resize-image","pytrends","pytz",
#             "pytz-deprecation-shim","pywin32","PyYAML","rake-nltk","regex","requests",
#             "requests-oauthlib","resize-right-sdk","rich","rsa","scipy","semver","sentry-sdk",
#             "setproctitle","setuptools","shortuuid","six","smmap","sniffio","soupsieve",
#             "stanfordcorenlp","stanza","starlette","streamlit","termcolor","toml","toolz","torch",
#             "torchaudio","torchvision","tornado","tqdm","typing_extensions","tzdata","tzlocal",
#             "uritemplate","urllib3","uvicorn","validators","wandb","watchdog","watchfiles","wcwidth",
#             "webencodings","websocket-client","websockets","windows-curses","xmltodict","yapf","yarl",
#             "zipp"]

    libs = ["language-tool-python","stanza","torch"]

    for lib in libs:
        os.system("pip install "+lib+" -i https://pypi.tuna.tsinghua.edu.cn/simple")
