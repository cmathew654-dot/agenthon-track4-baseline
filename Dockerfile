FROM python:3.13-slim@sha256:70729b46c69b4f1e97c4822c1af3df53a1476cf5ddc6c087c0c10bc3a5678c2f
LABEL qfbench2.interface_version="2.0"
LABEL org.opencontainers.image.title="Agenthon Track 4 minimal baseline"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.description="Locally modified model-free baseline with manifest-bound entity citations; source repository not yet published"
LABEL net.agenthon.baseline.upstream.source="https://github.com/Agenthon-2026/track4-analysis-public"
LABEL net.agenthon.baseline.upstream.revision="eef782bf5a92f4cc9a1a1522d766adde9f8a09a5"
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY baseline_agent/*.py ./baseline_agent/
COPY baseline_agent.py LICENSE ./
USER 65534:65534
ENTRYPOINT ["python", "/app/baseline_agent.py"]
CMD ["analyze", "--help"]
