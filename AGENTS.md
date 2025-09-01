# AGENTS.md

This repository is structured to reflect a top-tier tech company. All agent profiles are located in the numbered directories, organized by their function and seniority.

## Agent Naming Convention

All agent profiles are named using the `[3-letter-short-form]-guardian.md` schema. For example, the Chief Product Officer agent is named `cpo-guardian.md`.

## Company Hierarchy

```mermaid
graph TD
    subgraph "1-product"
        subgraph "1-product-management"
            cpo("cpo-guardian.md")
            subgraph "1-product-strategy"
                pds("pds-guardian.md")
                psm("psm-guardian.md")
            end
            subgraph "2-product-ownership"
                ppo("ppo-guardian.md")
                spo("spo-guardian.md")
                apo("apo-guardian.md")
            end
        end
        subgraph "2-product-design"
            cpd("cpd-guardian.md")
            subgraph "1-ux-research"
                uxr("uxr-guardian.md")
                jur("jur-guardian.md")
            end
            subgraph "2-ui-design"
                uid("uid-guardian.md")
                jui("jui-guardian.md")
            end
        end
    end

    subgraph "2-engineering"
        subgraph "1-cto-office"
            cto("cto-guardian.md")
            tfe("tfe-guardian.md")
        end
        subgraph "2-software-engineering"
            vps("vps-guardian.md")
            subgraph "1-architecture"
                par("par-guardian.md")
                sar("sar-guardian.md")
            end
            subgraph "2-backend-engineering"
                dbe("dbe-guardian.md")
                sbe("sbe-guardian.md")
                jbe("jbe-guardian.md")
            end
            subgraph "3-frontend-engineering"
                dfe("dfe-guardian.md")
                sfe("sfe-guardian.md")
                jfe("jfe-guardian.md")
            end
            subgraph "4-mobile-engineering"
                dme("dme-guardian.md")
                sme("sme-guardian.md")
                jme("jme-guardian.md")
            end
        end
        subgraph "3-quality-engineering"
            dqe("dqe-guardian.md")
            sqe("sqe-guardian.md")
            jqe("jqe-guardian.md")
        end
        subgraph "4-devops-engineering"
            dde("dde-guardian.md")
            sde("sde-guardian.md")
            jde("jde-guardian.md")
        end
    end

    subgraph "3-operations"
        subgraph "1-coo-office"
            coo("coo-guardian.md")
        end
        subgraph "2-security-operations"
            dso("dso-guardian.md")
            sse("sse-guardian.md")
            jse("jse-guardian.md")
        end
        subgraph "3-data-operations"
            ddo("ddo-guardian.md")
            sde_do("sde-guardian.md")
            jde_do("jde-guardian.md")
        end
        subgraph "4-it-operations"
            dio("dio-guardian.md")
            sit("sit-guardian.md")
            jit("jit-guardian.md")
        end
    end

    cpo --> pds
    pds --> psm
    cpo --> ppo
    ppo --> spo
    spo --> apo
    cpd --> uxr
    uxr --> jur
    cpd --> uid
    uid --> jui
    cto --> tfe
    cto --> vps
    vps --> par
    par --> sar
    vps --> dbe
    dbe --> sbe
    sbe --> jbe
    vps --> dfe
    dfe --> sfe
    sfe --> jfe
    vps --> dme
    dme --> sme
    sme --> jme
    vps --> dqe
    dqe --> sqe
    sqe --> jqe
    vps --> dde
    dde --> sde
    sde --> jde
    coo --> dso
    dso --> sse
    sse --> jse
    coo --> ddo
    ddo --> sde_do
    sde_do --> jde_do
    coo --> dio
    dio --> sit
    sit --> jit
```

## How to Use

When you need to perform a task, first identify the appropriate agent by reviewing the folder structure and agent profiles. The directory structure reflects the hierarchy of a top-tier tech company, with senior roles in higher-level directories and junior roles in lower-level directories. Then, follow the instructions in the agent's profile to complete the task.
