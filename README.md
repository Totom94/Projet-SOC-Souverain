# 🛡️ SOC Souverain Automatisé - Architecture Cloud & On-Premise


## 📝 Présentation du Projet
Ce projet consiste en la mise en place d'un **Centre d'Opérations de Sécurité (SOC)** complet et automatisé, déployé sur l'infrastructure **Airbus CyberRange**. L'objectif est de fournir une solution souveraine de détection et de réponse aux incidents, adaptée aux besoins des infrastructures critiques et des PME.

---

## 🏗️ Architecture Réseau
> Voici la topologie déployée. Elle sépare les zones d'attaques, de services et de management.


*Note : Le cœur du réseau est géré par un firewall pfSense filtrant les flux entre les VLANs d'attaques et les cibles.*

---

## 🚀 Stack Technologique & Flux
Le workflow suit la logique **Détecter -> Analyser -> Répondre** :

| Composant | Rôle |
| :--- | :--- |
| **pfSense / Suricata** | Segmentation réseau et IDS (Intrusion Detection System). |
| **Wazuh** | SIEM & EDR : Collecte des logs et détection d'anomalies. |
| **n8n** | SOAR : Orchestration des alertes via Webhooks. |
| **TheHive / Cortex** | IRP : Gestion des incidents et analyse de fichiers (VirusTotal). |
| **MISP** | Threat Intelligence : Partage et corrélation d'IOCs. |

---

## 📂 Structure du Dépôt
* `📂 architecture` : Diagrammes réseau et flux de données.
* `📂 attaques` : Scénarios de tests (Kali vs Windows/DVWA).
* `📂 cortex` : Installation et configuration complète.
* `📂 livrables` : Poster technique, rapport technique et rapport d'expertise.
* `📂 misp` : Installation et configuration complète.
* `📂 n8n` : Installation et configuration complète.
* `📂 pfsense` : Configuration complète.
* `📂 thehive` : Installation et configuration complète.
* `📂 wazuh` : Installation et configuration complète.
