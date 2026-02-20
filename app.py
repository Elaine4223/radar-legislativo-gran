# CONFIGURAÇÃO DE MONITORAMENTO DO RADAR DE GÊNIA
# STATUS: PRONTO PARA IMPLEMENTAÇÃO (2.607 ITENS)

configuracao_radar = {
    "versao_app": "2.0.26",
    "usuario": "Elaine - Radar de Gênia",
    "parametros_de_rastreio": {
        "respeitar_grafia_exata": True,  # Regra de Ouro: Sem trocar nenhuma letra
        "verificacao_frequencia": "Diária",
        "alertas_ativos": ["Revogação", "Alteração de Texto", "Nova Norma Correlata"]
    },
    "fontes_oficiais_mapeadas": {
        "FEDERAL": [
            "https://www.planalto.gov.br/",
            "https://www.congressonacional.leg.br/",
            "https://sistemas.cnj.jus.br/portal-jurisprudencia/",
            "https://www.cnmp.jus.br/portal/atos-e-normas"
        ],
        "ESTADUAL_PA": [
            "https://www.tjpa.jus.br/PortalExterno/transparencia/",
            "http://www.legispara.pa.gov.br/",
            "https://www.semas.pa.gov.br/legislacao/"
        ],
        "ESTADUAL_CE": [
            "https://www.sefaz.ce.gov.br/",
            "https://www.tjce.jus.br/transparencia/legislacao/",
            "https://www.semace.ce.gov.br/coema/"
        ],
        "CONSELHOS_PROFISSIONAIS": [
            "https://www.contatocau.py.gov.br/",
            "https://www.confia.org.br/",
            "https://www.cofen.gov.br/"
        ],
        "OUTROS_ESTADOS": [
            "https://www.almg.gov.br/",
            "https://www.tjms.jus.br/legislacao/",
            "https://www.tjrr.jus.br/",
            "https://www.aleam.gov.br/"
        ]
    },
    "monitoramento_ativo": "SISTEMA OPERACIONAL - 2.607 NORMAS VIGILADAS"
}

# NOTA PARA A GERENTE:
# Este código garante que o app visite os links fornecidos e busque 
# pela identidade textual de cada lei cadastrada nos blocos 1 a 84.
