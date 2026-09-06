# ML Integration, Multipage Apps, Themes, and Deployment

## ML model integration

Load/train the model once with `cache_resource`, keep feature order/names stable,
validate ranges, and show limitations. Never present model confidence as truth.

```python
@st.cache_resource
def get_model():
    model = RandomForestClassifier(random_state=42)
    return model.fit(features, target)
```

Production ML apps also need model versioning, preprocessing parity, drift and
quality monitoring, access control, privacy review, and safe fallback behavior.

## Multipage apps

A simple structure is:

```text
multipage_app/
├── Home.py
└── pages/
    ├── 1_Data.py
    └── 2_Charts.py
```

Run `streamlit run multipage_app/Home.py`. For more control, use Streamlit's
programmatic navigation APIs. Keep shared functions in ordinary modules rather
than importing page scripts with side effects.

## Themes/configuration

Project configuration lives in `.streamlit/config.toml`. Commit harmless theme
and server defaults, but keep secrets out of Git. Use environment variables or
the deployment platform's secrets facility and access configured secrets through
`st.secrets` only when present.

## Deployment checklist

- Pin/test dependencies and select the correct entry file.
- Keep secrets outside source control.
- Use paths based on `Path(__file__)`, not the launch directory.
- Cache expensive deterministic work; bound cache growth.
- Handle missing files, empty uploads, and external-service failures.
- Avoid global mutable state for per-user data; use session state/database.
- Add authentication/authorization if data is private.
- Monitor errors, latency, resource use, and model/data quality.
- Respect memory/CPU/upload limits of the hosting platform.

Deployment choices include Streamlit Community Cloud, containers, or another
Python hosting platform. Platform steps change over time; check its current
official documentation when publishing.
