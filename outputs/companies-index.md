# Companies index

**237 companies.** A generated **view** over `companies.jsonl` — never edit it, regenerate it.
**211 enriched · 9 partially recovered · 17 unreachable** of 237. Regenerated 2026-08-11.

Pull a full record by id:

```bash
grep '"company_id": "braze"' outputs/companies.jsonl | jq .
jq -c 'select(.category_count>=5) | {company, channels:.enrichment.channels.value}' outputs/companies.jsonl
```

`Src` — **B** both sources · **G** Gartner only · **2** G2 only.  
`St` — **D** done · **P** partially recovered (domain confirmed, marketing site blocked) · **U** unreachable.  
`Ch` / `Ind` — count of channels / industries served.  
A dash means `UNKNOWN`: not found within the fixed four-fetch budget, which is a finding, not a gap in effort.

| Company | HQ | Founded | Status | Deployment | Ch | Ind | Cats | Src | St | F |
|---|---|---|---|---|---|---|---|---|---|---|
| Salesforce | US | 1999 | — | — | — | — | 7 | B | D | 4 |
| Braze | — | — | — | — | 6 | 8 | 6 | B | D | 4 |
| Dotdigital | — | — | — | — | 2 | — | 6 | B | D | 3 |
| Adobe | — | — | — | — | — | — | 5 | B | P | 0 |
| Brevo | United States | — | — | — | 5 | — | 5 | B | D | 4 |
| Customer.io | US | 2012 | — | — | 6 | 6 | 5 | B | D | 4 |
| Iterable | — | — | — | — | 4 | — | 5 | B | D | 3 |
| Klaviyo | US | 2012 | — | — | 6 | — | 5 | B | D | 4 |
| MoEngage | — | 2014 | — | — | 7 | — | 5 | B | D | 3 |
| Netmera | — | — | — | — | 6 | 12 | 5 | B | D | 3 |
| Acoustic | US | 2019 | — | — | 3 | 12 | 4 | G | D | 4 |
| ActiveCampaign | — | 2003 | — | — | 3 | — | 4 | B | D | 4 |
| Attentive | US | 2016 | — | — | 4 | — | 4 | B | D | 4 |
| CleverTap | IN | — | — | — | 6 | — | 4 | G | D | 4 |
| Insider One | — | — | — | — | 6 | 8 | 4 | B | D | 4 |
| Intuit | US | 1983 | — | — | 1 | — | 4 | B | D | 4 |
| Oracle | — | — | legacy | — | 2 | — | 4 | G | D | 3 |
| SAP | — | — | legacy | — | — | — | 4 | G | U | 0 |
| WebEngage | — | — | — | — | 7 | — | 4 | B | D | 4 |
| Zoho | — | — | — | — | 1 | — | 4 | B | D | 3 |
| Constant Contact | — | — | — | — | — | — | 3 | B | P | 0 |
| Conversion | — | — | — | — | — | — | 3 | G | D | 3 |
| Cordial | US | 2014 | — | — | 4 | — | 3 | G | D | 4 |
| Epsilon | — | 1968 | — | — | 1 | 12 | 3 | B | D | 3 |
| HubSpot | US | 2006 | — | — | — | — | 3 | B | D | 4 |
| Netcore | — | — | — | — | 8 | — | 3 | G | D | 4 |
| Omnisend | — | — | — | — | 4 | — | 3 | B | D | 4 |
| Pushwoosh | — | 2014 | — | — | 8 | — | 3 | G | D | 4 |
| Smart Communications | — | — | — | — | — | 11 | 3 | G | D | 3 |
| Tech Mahindra | IN | — | — | — | 1 | 12 | 3 | G | D | 3 |
| Upland | — | — | legacy | — | — | — | 3 | G | D | 2 |
| Wigzo | — | — | — | — | — | — | 3 | G | U | 0 |
| Xtremepush | IE | 2015 | — | — | — | — | 3 | G | D | 3 |
| Zeta | — | — | — | — | 1 | — | 3 | G | D | 3 |
| Acquia | US | 2007 | — | api-platform | — | — | 2 | G | D | 4 |
| Act-On | — | — | — | — | 1 | 12 | 2 | G | D | 4 |
| Airship | — | 2019 | — | — | 4 | 12 | 2 | G | D | 4 |
| Bird | — | — | — | — | 6 | — | 2 | G | D | 4 |
| Bloomreach | — | — | — | — | 5 | 12 | 2 | B | D | 4 |
| Bluecore | — | — | — | — | 3 | — | 2 | G | D | 4 |
| Capillary Technologies | — | — | — | — | — | 7 | 2 | G | D | 3 |
| Cisco Systems | — | — | — | — | — | — | 2 | G | U | 0 |
| Clear C2 | — | — | — | — | — | — | 2 | G | D | 2 |
| ContactPigeon | — | — | — | — | — | — | 2 | G | D | 2 |
| Corefactors | US | — | — | — | — | — | 2 | G | D | 4 |
| D-engage | — | — | — | on-premise | 7 | — | 2 | G | D | 4 |
| Diennea | — | — | — | — | — | — | 2 | G | D | 2 |
| EVAM | — | — | — | — | 4 | 12 | 2 | B | D | 3 |
| HighLevel | — | — | — | — | 2 | — | 2 | 2 | D | 3 |
| inConcert | — | — | — | — | 1 | — | 2 | G | D | 3 |
| indigitall | — | — | — | — | 7 | 12 | 2 | G | D | 3 |
| iPresso | — | — | — | — | 5 | 12 | 2 | G | D | 4 |
| Listrak | — | — | — | — | 4 | — | 2 | G | D | 3 |
| Maestra.io | US | 2022 | — | — | 6 | — | 2 | G | D | 4 |
| MailerLite | — | — | — | — | 1 | — | 2 | B | D | 4 |
| Maropost | — | — | — | — | 3 | — | 2 | G | D | 4 |
| MessageGears | — | — | — | — | — | — | 2 | G | P | 0 |
| Microsoft | — | — | legacy | — | — | — | 2 | G | D | 4 |
| Mindmatrix | US | 1998 | — | — | — | — | 2 | G | D | 3 |
| NewZapp | — | — | — | — | — | — | 2 | G | U | 0 |
| Nvecta | — | — | — | — | 7 | 12 | 2 | G | D | 3 |
| OneSignal | — | — | — | — | 6 | 12 | 2 | G | D | 4 |
| OptiKPI | — | — | — | — | 4 | 12 | 2 | G | D | 4 |
| Optimove | — | — | — | — | 6 | 12 | 2 | G | D | 3 |
| Pegasystems | — | — | — | — | — | — | 2 | G | D | 4 |
| Pipedrive | — | 2010 | — | on-premise | 2 | — | 2 | B | D | 4 |
| Rapidops | — | — | — | managed-service | 1 | 12 | 2 | G | D | 3 |
| Salesmsg | — | — | — | — | 1 | — | 2 | B | D | 2 |
| Sender | — | 2012 | — | — | 2 | — | 2 | B | D | 4 |
| Sinch | — | — | — | saas-single-tenant | 6 | — | 2 | B | D | 4 |
| SproutLoud | United States | — | — | — | 2 | — | 2 | G | D | 4 |
| Tidio | — | — | — | — | 3 | 12 | 2 | G | D | 4 |
| Touchdown | — | — | — | — | — | — | 2 | G | D | 2 |
| Trueblue | — | — | — | — | — | — | 2 | G | D | 2 |
| Voyado | — | — | — | — | 3 | — | 2 | G | D | 4 |
| Webmaxy | — | — | — | — | 5 | 3 | 2 | G | D | 4 |
| Webmecanik | — | — | — | — | — | — | 2 | G | D | 2 |
| ZEPIC | — | — | — | — | 5 | 12 | 2 | G | D | 4 |
| adnymics | — | — | — | — | — | — | 1 | G | D | 2 |
| AEvent | — | — | — | — | — | — | 1 | G | D | 4 |
| AfterShip | — | — | — | — | — | — | 1 | G | P | 0 |
| Agillic | — | — | — | on-premise | 1 | — | 1 | G | D | 4 |
| Aislelabs | — | — | — | — | 2 | 12 | 1 | G | D | 4 |
| Alterian | — | — | — | — | — | — | 1 | G | D | 4 |
| Amazing Mail | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Amazon Web Services | — | 2006 | — | — | — | 6 | 1 | G | D | 3 |
| Appier | — | — | — | — | 1 | 12 | 1 | G | D | 3 |
| AT Internet | — | — | — | — | — | — | 1 | G | U | 0 |
| AtomPark Software | — | — | — | — | 3 | — | 1 | G | D | 3 |
| AWeber | — | 1998 | — | — | 3 | — | 1 | G | D | 3 |
| Barilliance | — | — | — | — | 3 | — | 1 | G | D | 4 |
| Base | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Beaconsmind | — | — | — | — | — | — | 1 | G | U | 0 |
| Benchmark Email | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Birdeye | — | — | — | — | — | — | 1 | 2 | D | 2 |
| BiteSpeed | — | — | — | — | 4 | — | 1 | G | D | 2 |
| Blueshift | — | — | — | private-cloud | 5 | 12 | 1 | G | D | 4 |
| BrandOps | — | — | — | — | — | — | 1 | G | D | 2 |
| Bridgeline Digital | — | — | — | — | — | — | 1 | G | D | 3 |
| BSI Software | — | — | — | — | — | 7 | 1 | G | D | 3 |
| BUSINESSNEXT | — | — | — | — | — | — | 1 | G | D | 3 |
| CAKE | — | — | — | — | 2 | — | 1 | G | D | 4 |
| Campaigner | — | — | — | — | 2 | — | 1 | G | D | 4 |
| CentraHub | — | — | — | — | 2 | — | 1 | G | D | 4 |
| ChannelMix | — | — | — | — | — | — | 1 | G | D | 2 |
| ClickDimensions | — | — | — | — | — | — | 1 | G | U | 0 |
| Close | — | 2013 | — | — | — | — | 1 | 2 | D | 4 |
| Creatio | — | — | — | — | — | 12 | 1 | G | D | 4 |
| Critical Impact | — | — | — | — | 1 | — | 1 | G | D | 2 |
| CustomerInsights.ai | — | — | — | — | — | — | 1 | G | D | 3 |
| DANAconnect | — | — | — | — | 5 | — | 1 | G | D | 3 |
| Datorama | — | — | — | — | — | — | 1 | G | U | 0 |
| Delivra | — | — | — | — | 2 | — | 1 | G | D | 4 |
| Digitalbox | — | — | — | — | — | — | 1 | G | D | 2 |
| Duda | — | — | — | — | — | — | 1 | 2 | D | 2 |
| Dyrect | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Dyspatch | — | — | — | — | 4 | — | 1 | G | D | 4 |
| E-goi | — | — | — | — | — | — | 1 | G | D | 2 |
| Ecomail | CZ | — | — | — | 2 | — | 1 | G | D | 4 |
| EcoSend | — | — | — | — | 2 | — | 1 | G | D | 4 |
| Emailidea | — | — | — | — | — | — | 1 | G | U | 0 |
| Emma | — | — | — | — | — | — | 1 | 2 | D | 3 |
| EngageBay Inc | — | 2017 | — | — | 5 | — | 1 | 2 | D | 3 |
| Entirely | CH | — | — | — | — | — | 1 | G | D | 2 |
| EZ Texting | US | — | — | — | 4 | 12 | 1 | 2 | D | 4 |
| Flodesk | — | — | — | — | 2 | — | 1 | 2 | D | 4 |
| FlowUp | — | — | — | — | — | — | 1 | G | D | 2 |
| FollowAnalytics | — | — | — | — | — | — | 1 | G | U | 0 |
| Foursquare | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Free Stand Sampling Solutions | — | — | — | — | — | — | 1 | G | D | 3 |
| Fresh Relevance | — | — | — | — | — | — | 1 | G | U | 0 |
| Freshworks | — | — | — | — | — | — | 1 | G | P | 0 |
| Frizbit | — | — | — | — | 5 | — | 1 | G | D | 4 |
| GetResponse | PL | 1998 | — | — | 6 | — | 1 | 2 | D | 4 |
| GMass | — | — | — | — | 3 | — | 1 | 2 | D | 4 |
| GoSquared | — | — | — | — | — | — | 1 | G | D | 2 |
| Grey Box | — | — | — | — | — | — | 1 | G | D | 2 |
| HCLTech | — | — | — | on-premise, managed-service | 1 | 12 | 1 | G | D | 3 |
| Health Chain | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Hewlett Packard Enterprise | — | — | — | — | — | — | 1 | G | U | 0 |
| Hey Sid | — | — | — | — | — | — | 1 | G | D | 2 |
| HOLLYFY | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Hostinger | — | 2004 | — | — | 1 | — | 1 | G | D | 4 |
| IBM | — | — | — | — | — | — | 1 | G | D | 3 |
| iContact | — | — | — | — | 1 | 12 | 1 | G | D | 4 |
| InAppStory | PT | — | — | on-premise | 2 | — | 1 | G | D | 4 |
| Inflection.io | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Insightly | — | — | — | — | — | — | 1 | G | D | 2 |
| Inspired Thinking Group | — | — | — | — | — | — | 1 | G | D | 3 |
| Instantly | — | — | — | — | 1 | — | 1 | 2 | D | 4 |
| Intense Technologies | — | — | — | — | — | — | 1 | G | U | 0 |
| Iorta TechNxt | Malaysia | 2023 | — | — | — | — | 1 | G | D | 2 |
| IQVIA | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Kenyt.AI | — | — | — | — | — | — | 1 | G | D | 3 |
| L-Soft | — | — | — | — | 1 | 12 | 1 | G | D | 3 |
| Leadspicker | — | — | — | on-premise | 1 | — | 1 | G | D | 4 |
| LeadSquared | — | — | — | — | 1 | 12 | 1 | G | D | 4 |
| LeadsRx | — | — | — | — | — | — | 1 | G | D | 4 |
| lemlist | — | — | — | — | 4 | — | 1 | 2 | D | 4 |
| Levitate | — | — | — | — | — | — | 1 | 2 | D | 2 |
| Lob | US | — | — | — | 1 | 12 | 1 | G | D | 4 |
| Longtail UX | — | — | — | — | — | — | 1 | G | U | 0 |
| Mailgun | — | — | — | — | 2 | — | 1 | 2 | D | 4 |
| Mapp | — | — | — | — | 2 | — | 1 | G | D | 4 |
| Marigold | — | — | — | — | — | — | 1 | G | D | 2 |
| MarketingPlatform | — | — | — | — | 2 | — | 1 | G | D | 4 |
| Marketplacer | — | — | — | — | — | — | 1 | G | D | 4 |
| Mastercard | — | — | — | — | — | — | 1 | G | P | 0 |
| Medallia | — | — | — | — | 1 | 12 | 1 | G | D | 4 |
| Meiro | — | — | — | on-premise, self-hosted, private-cloud | 3 | 12 | 1 | G | D | 4 |
| Mekari | — | 2015 | — | — | 2 | — | 1 | G | D | 3 |
| Messangi | — | — | — | — | 6 | — | 1 | G | D | 3 |
| Metadata | US | 2015 | — | — | 2 | — | 1 | G | D | 3 |
| MINT | — | — | — | — | — | — | 1 | G | D | 3 |
| MobiMesh | — | — | — | — | — | — | 1 | G | D | 2 |
| Mobivity | — | — | — | — | — | — | 1 | G | D | 2 |
| NerdMonster Digital Retail | — | — | — | — | — | — | 1 | G | D | 3 |
| OBASE | — | — | — | — | — | — | 1 | G | D | 3 |
| Ometria | — | — | — | — | 5 | — | 1 | G | D | 4 |
| ONLINECITY.IO | — | — | — | — | — | — | 1 | G | D | 2 |
| Ortto | — | — | — | — | — | — | 1 | G | D | 2 |
| PAR | — | — | — | — | — | — | 1 | G | U | 0 |
| Perion | — | — | — | — | — | — | 1 | G | D | 3 |
| Pitney Bowes | — | — | — | — | 1 | 12 | 1 | G | D | 3 |
| Piwik PRO | — | — | — | — | 1 | 12 | 1 | G | D | 4 |
| Podium | — | — | — | — | 1 | — | 1 | 2 | D | 3 |
| Postal | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Postalytics | — | — | — | — | 2 | 12 | 1 | G | D | 3 |
| PostcardMania | — | — | — | — | — | — | 1 | G | P | 0 |
| PostGrid | — | — | — | — | — | — | 1 | G | P | 0 |
| Precisely | — | 1968 | legacy | — | 3 | 12 | 1 | G | D | 3 |
| Printfection | — | — | — | — | — | — | 1 | G | D | 4 |
| Pyze | — | — | — | private-cloud | — | 12 | 1 | G | D | 4 |
| Qujam | US | 2023 | — | — | — | — | 1 | G | D | 4 |
| Radar | USA | 2016 | — | — | — | 6 | 1 | G | D | 4 |
| Reachdesk | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Redpoint | — | — | — | — | — | — | 1 | G | D | 3 |
| Rejoiner | — | — | — | — | 3 | — | 1 | G | D | 4 |
| Resulticks | — | — | — | — | — | — | 1 | G | D | 2 |
| Reteno | PL | — | — | — | 4 | — | 1 | G | D | 4 |
| Rocket Now | CA | 2020 | — | — | — | — | 1 | G | D | 2 |
| SALESmanago | PL | — | — | — | — | — | 1 | G | D | 4 |
| SAS | — | — | legacy | — | — | 12 | 1 | G | D | 3 |
| Sendoso | — | — | — | — | 1 | — | 1 | G | D | 3 |
| SendPulse | — | 2015 | — | — | 7 | — | 1 | G | D | 4 |
| Sensors Data | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Sitecore | US | 2001 | — | — | 1 | — | 1 | G | D | 3 |
| SlickText | — | 2012 | — | — | 4 | — | 1 | 2 | D | 4 |
| Soprano | — | — | — | — | — | — | 1 | G | D | 2 |
| Spectrm | — | — | — | — | — | — | 1 | G | U | 0 |
| SpiceSend | — | — | legacy | — | 1 | — | 1 | G | D | 3 |
| Splio | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Sprinklr | United States | — | — | — | 5 | 12 | 1 | G | D | 4 |
| Storyly | US | 2020 | — | — | — | — | 1 | G | D | 3 |
| Striker Soft Solutions | — | — | — | — | — | — | 1 | G | U | 0 |
| SugarAI | — | — | — | — | — | 2 | 1 | G | D | 4 |
| SwiftERM Hyper-Personalisation | United Kingdom | — | — | — | 3 | — | 1 | G | D | 3 |
| Swrve | — | — | — | — | — | — | 1 | G | P | 0 |
| Text | US | 2023 | — | — | 5 | 2 | 1 | G | D | 4 |
| Textedly | — | — | — | — | 5 | 12 | 1 | 2 | D | 4 |
| Thryv | US | 2013 | — | — | 2 | 12 | 1 | G | D | 4 |
| Treasure AI | US | 2011 | — | — | 2 | 12 | 1 | G | D | 4 |
| Trendemon | — | — | — | — | 3 | — | 1 | G | D | 4 |
| Twilio | — | — | — | — | 5 | — | 1 | G | D | 4 |
| Upaknee | — | — | — | managed-service | 1 | — | 1 | G | D | 3 |
| UTM.io | — | — | — | — | — | — | 1 | G | D | 4 |
| ValueFirst | — | — | — | — | — | — | 1 | G | D | 2 |
| Veloxy IO | — | — | — | — | — | — | 1 | G | D | 4 |
| VeryUtils | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Vibes | — | — | — | — | 4 | 12 | 1 | G | D | 4 |
| Warmy | — | — | — | — | 1 | — | 1 | G | D | 4 |
| Webflow | US | 2013 | — | — | — | — | 1 | 2 | D | 4 |
| WILY | — | — | — | — | — | — | 1 | G | D | 2 |
| Woosmap | — | — | — | — | 1 | 12 | 1 | G | D | 4 |
| WorksBuddy | — | 2024 | — | — | 2 | 9 | 1 | G | D | 4 |
| xiQ | — | — | — | — | 1 | — | 1 | G | D | 3 |
| Yotpo | — | — | — | — | 4 | — | 1 | G | D | 4 |
