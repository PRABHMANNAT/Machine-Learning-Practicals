# Focused Streamlit demos

Run one lesson at a time from the `14-Streamlit` folder:

```powershell
streamlit run demos/08-charts.py
```

Each numbered file teaches one idea with tiny data, two or more visible
components, beginner comments, and explanations of important parameters.

| Files | Topics |
| --- | --- |
| 01–07 | Text/media basics, widgets, layout, state, caching, data, status |
| 08–12 | Charts, authentication, connections, images/video, audio |
| 13–17 | Text, maps, DataFrames, graphs, molecules/genes |
| 18–22 | Code editors, navigation, developer tools, integrations, LLM chat |

The authentication page contains a pretend local login so it works without
secrets. Read its OIDC section and copy `.streamlit/secrets.toml.example` when
you are ready to configure a real identity provider.

The LLM page is deliberately local and deterministic. It teaches prompts,
chat history, temperature, output length, and the `st-chat-message` UI without
charging an API account or requiring a key.
