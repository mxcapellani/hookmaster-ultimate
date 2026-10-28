# HOOKMASTER ULTIMATE — CLONE DE GANCHOS | CLONE DIGITAL

Versão 1.0.0.

Skill profissional de criação, análise, otimização e clonagem estrutural de hooks para TikTok, Reels e Shorts, com técnicas de retenção, biblioteca de padrões virais, personalização de linguagem, testes A/B e direção visual.

## Finalidade e experiência
Transformar temas em aberturas curtas, com assunto imediato e uma razão para continuar assistindo. Entrega padrão: cinco opções de duas linhas, respeitando quantidade e estilo pedidos. Não é um gerador de roteiros longos ou garantia de viralização.

## Cobertura das 50 funções
As 50 funcionalidades fornecidas estão integralmente nomeadas e descritas no [núcleo](.agents/skills/hookmaster-ultimate/SKILL.md) e na [fonte original](docs/SOURCE_SPECIFICATION.md). Funções 01–19: identificadas na especificação; 20: biblioteca externa citada; 21–50: melhorias Ultimate propostas. Isso não equivale a execução comparativa comprovada.

Preservação: detectores de atraso, confusão, irrelevância e desinteresse; cinco ângulos, doze tons, criação por tema, assunto nos primeiros segundos e direção visual sob pedido.

Melhorias: revisão, pontuação ponderada, testes A/B, persona/nicho, diversificação, lotes, encurtamento, expansão, extração de moldes, análise de referências acessíveis, métricas fornecidas e consistência com roteiro.

## Biblioteca e direitos
A biblioteca de padrões próprios incluída é autoral e ilustrativa. “Viral” descreve a categoria de padrões, não resultado medido. O documento “1,000 Viral Hooks (PBL).docx” não foi anexado, analisado nem redistribuído. É uma referência externa relatada e não uma dependência obrigatória.

## Instalação e uso
Ver [instalação](docs/INSTALLATION.md). Colocar a pasta `.agents/skills/hookmaster-ultimate/` no diretório de descoberta aceito pelo seu agente. A publicação no GitHub não instala a Skill automaticamente no ChatGPT.

Exemplos:
- “Crie cinco hooks sobre produtividade.”
- “Reescreva esta abertura mantendo a promessa.”
- “Extraia a estrutura desta referência e adapte a outro nicho.”
- “Crie A/B mudando apenas o ângulo inicial.”

## Estrutura e evidência
Núcleo autossuficiente; três referências; exemplos completos; auditoria e especificação em docs; vinte casos comparativos; validador e testes; workflow CI. O anexo original foi preservado integralmente na documentação.

## Dependências, permissões e limites
Texto básico não precisa de internet nem serviços. Leitura de materiais depende do host e do arquivo. Não há métricas automáticas nem publicação automática. Sem acesso, solicitar conteúdo; não pedir credenciais. Memória usa apenas contexto disponível. Não garantir viralização, visualizações ou compatibilidade atual de APIs.

## Validação
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python tests/test_validator.py
```
Python 3.9+ e PyYAML 6.x; o validador funciona localmente após instalar a dependência, sem credenciais. GitHub Actions configurado para push e pull request. Testes estruturais não medem performance de hooks. [Comparação comportamental](docs/COMPARATIVE_TESTS.md) permanece não executada até registro real.

## Manutenção e licença
Consultar [histórico](CHANGELOG.md) e [contribuições](CONTRIBUTING.md). MIT, copyright 2026 mxcapellani. Atualizar mantendo o fluxo e a distinção entre evidências e extensões.
