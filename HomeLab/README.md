# Homelab — GPU-Accelerated NIDS

A network intrusion detection system based on GPU-acceleration.
- Working in small parts

## Components
- Host and target VM
- Nvidia RTX 3090 24GB
- Router
- Kiosk tablet

## Progress

- [ ] **1 · Boot one VM** — done when a Linux desktop loads
- [ ] **2 · Wire the network** — done when VM reaches internet + host pings VM
- [ ] **3 · Watch traffic** — done when I see my own browsing in the flow logs
- [ ] **4 · Flag the weird** — done when a tree model scores a flow normal vs odd
- [ ] **5 · Put it on the wall** — done when live flows show on the touch-panel

## Log

### Brick 1 — Boot one VM
_What I did:_ Installed VirtualBox, Installed the Ubuntu LTS, Configured it with 8GB RAM and 2 CPU:s and booted Ubuntu Desktop (LTS).
_Screenshot:_ <img width="1273" height="874" alt="Näyttökuva 2026-07-05 152934" src="https://github.com/user-attachments/assets/8005543b-b3c5-4c90-8f0c-8ccb66b4961a" />
