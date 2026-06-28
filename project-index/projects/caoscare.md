# CAOSCare / CareAware

Status: active, but secondary behind the dating service for this weekend.

## Core thesis

CAOSCare is a senior-care room/building intelligence system. It is not just an AI speaker. It watches, routes, escalates, assists, documents, and supports resident/staff workflows.

## Current hardware separation

Main workstation stays stable:

- Lenovo laptop
- Sony KDL-55EX640 TV
- HDMI mirror
- Roku Streambar audio target

CAOSCare node uses separate hardware:

- HP Elite mini PC / CAOSCare Node 1
- Separate monitor for setup
- Ethernet
- SSH after setup
- eMeet speaker/mic belongs to CAOSCare node

## Known repos

- `caosos/CAOSCARE.COM`
- `caosos/caos-care-node`

## Product areas

- Resident voice interaction
- Staff routing
- Maintenance awareness
- Thermostat / room comfort context
- Fire panel / building systems awareness, read-only and vendor-safe
- Family communication
- Documentation support
- Facility dashboard
- Alert/escalation logic
- Local node behavior
- Home Assistant integration
- Possible local voice stack: Whisper / Piper / Ollama as appropriate

## Conversation sources to inspect

- `HP EliteDesk Server Setup`
- `Ubuntu HDMI Mirror / Sony TV Troubleshooting`
- Brookdale maintenance/workflow conversations
- CAOSCare / Topicon NDA and hardware evaluation files

## Search terms

`CAOSCare`, `CareAware`, `senior care`, `resident`, `Home Assistant`, `HP Elite`, `node`, `eMeet`, `fire panel`, `thermostat`, `Brookdale`, `staff routing`, `alert`, `escalation`

## Current caution

Do not disturb the Lenovo/Sony/Roku working setup while building CAOSCare Node 1. Use separate monitor, Ethernet, and SSH.
