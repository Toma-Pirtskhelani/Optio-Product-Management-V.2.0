# Companies index

**237 companies.** A generated **view** over `companies.jsonl` — never edit it, regenerate it.
Enriched so far: **27 of 237**. Regenerated 2026-08-11.

Pull a full record by id:

```bash
grep '"company_id": "braze"' outputs/companies.jsonl | jq .
jq -c 'select(.category_count>=5) | {company, channels:.enrichment.channels.value}' outputs/companies.jsonl
```

`Src` — **B** both sources · **G** Gartner only · **2** G2 only.  
`St` — enrichment state: **N** not started · **D** done · **U** unreachable.  
`Ch` / `Ind` — count of channels / industries served.  
A dash means `UNKNOWN`: not found within the fixed four-fetch budget, which is a finding, not a gap in effort.

| Company | HQ | Founded | Status | Deployment | Ch | Ind | Cats | Src | St | F |
|---|---|---|---|---|---|---|---|---|---|---|
| Salesforce | US | — | — | — | — | — | 7 | B | D | 4 |
| Braze | — | — | — | — | 6 | 8 | 6 | B | D | 4 |
| Dotdigital | — | — | — | — | 2 | — | 6 | B | D | 3 |
| Adobe | — | — | — | — | — | — | 5 | B | U | 0 |
| Brevo | United States | — | — | — | 5 | — | 5 | B | D | 4 |
| Customer.io | US | 2012 | — | — | 6 | 6 | 5 | B | D | 4 |
| Iterable | — | — | — | — | 4 | — | 5 | B | D | 3 |
| Klaviyo | US | 2012 | — | — | 6 | — | 5 | B | D | 4 |
| MoEngage | — | — | — | — | 7 | — | 5 | B | D | 3 |
| Netmera | — | — | — | — | 6 | 12 | 5 | B | D | 3 |
| Acoustic | US | 2019 | — | — | 3 | 12 | 4 | G | D | 4 |
| ActiveCampaign | — | — | — | — | 3 | — | 4 | B | D | 4 |
| Attentive | US | 2016 | — | — | 4 | — | 4 | B | D | 4 |
| CleverTap | IN | — | — | — | 6 | — | 4 | G | D | 4 |
| Insider One | — | — | — | — | 6 | 8 | 4 | B | D | 4 |
| Intuit | US | 1983 | — | — | 1 | — | 4 | B | D | 4 |
| Oracle | — | — | legacy | — | 2 | — | 4 | G | D | 3 |
| SAP | — | — | legacy | — | — | — | 4 | G | U | 0 |
| WebEngage | — | — | — | — | 7 | — | 4 | B | D | 4 |
| Zoho | — | — | — | — | 1 | — | 4 | B | D | 3 |
| Constant Contact | — | — | — | — | — | — | 3 | B | U | 0 |
| Conversion | — | — | — | — | — | — | 3 | G | N | 0 |
| Cordial | US | 2014 | — | — | 4 | — | 3 | G | D | 4 |
| Epsilon | — | 1968 | — | — | 1 | 12 | 3 | B | D | 3 |
| HubSpot | US | 2006 | — | — | — | — | 3 | B | D | 4 |
| Netcore | — | — | — | — | 8 | — | 3 | G | D | 4 |
| Omnisend | — | — | — | — | 4 | — | 3 | B | D | 4 |
| Pushwoosh | — | — | — | — | — | — | 3 | G | N | 0 |
| Smart Communications | — | — | — | — | — | — | 3 | G | N | 0 |
| Tech Mahindra | IN | — | — | — | 1 | 12 | 3 | G | D | 3 |
| Upland | — | — | legacy | — | — | — | 3 | G | D | 2 |
| Wigzo | — | — | — | — | — | — | 3 | G | N | 0 |
| Xtremepush | IE | 2015 | — | — | — | — | 3 | G | D | 3 |
| Zeta | — | — | — | — | — | — | 3 | G | D | 2 |
| Acquia | — | — | — | — | — | — | 2 | G | N | 0 |
| Act-On | — | — | — | — | — | — | 2 | G | N | 0 |
| Airship | — | — | — | — | — | — | 2 | G | N | 0 |
| Bird | — | — | — | — | — | — | 2 | G | N | 0 |
| Bloomreach | — | — | — | — | — | — | 2 | B | N | 0 |
| Bluecore | — | — | — | — | — | — | 2 | G | N | 0 |
| Capillary Technologies | — | — | — | — | — | — | 2 | G | N | 0 |
| Cisco Systems | — | — | — | — | — | — | 2 | G | N | 0 |
| Clear C2 | — | — | — | — | — | — | 2 | G | N | 0 |
| ContactPigeon | — | — | — | — | — | — | 2 | G | N | 0 |
| Corefactors | — | — | — | — | — | — | 2 | G | N | 0 |
| D-engage | — | — | — | — | — | — | 2 | G | N | 0 |
| Diennea | — | — | — | — | — | — | 2 | G | N | 0 |
| EVAM | — | — | — | — | — | — | 2 | B | N | 0 |
| HighLevel | — | — | — | — | — | — | 2 | 2 | N | 0 |
| inConcert | — | — | — | — | — | — | 2 | G | N | 0 |
| indigitall | — | — | — | — | — | — | 2 | G | N | 0 |
| iPresso | — | — | — | — | — | — | 2 | G | N | 0 |
| Listrak | — | — | — | — | — | — | 2 | G | N | 0 |
| Maestra.io | — | — | — | — | — | — | 2 | G | N | 0 |
| MailerLite | — | — | — | — | — | — | 2 | B | N | 0 |
| Maropost | — | — | — | — | — | — | 2 | G | N | 0 |
| MessageGears | — | — | — | — | — | — | 2 | G | N | 0 |
| Microsoft | — | — | legacy | — | — | — | 2 | G | N | 0 |
| Mindmatrix | — | — | — | — | — | — | 2 | G | N | 0 |
| NewZapp | — | — | — | — | — | — | 2 | G | N | 0 |
| Nvecta | — | — | — | — | — | — | 2 | G | N | 0 |
| OneSignal | — | — | — | — | — | — | 2 | G | N | 0 |
| OptiKPI | — | — | — | — | — | — | 2 | G | N | 0 |
| Optimove | — | — | — | — | — | — | 2 | G | N | 0 |
| Pegasystems | — | — | — | — | — | — | 2 | G | N | 0 |
| Pipedrive | — | — | — | — | — | — | 2 | B | N | 0 |
| Rapidops | — | — | — | — | — | — | 2 | G | N | 0 |
| Salesmsg | — | — | — | — | — | — | 2 | B | N | 0 |
| Sender | — | — | — | — | — | — | 2 | B | N | 0 |
| Sinch | — | — | — | — | — | — | 2 | B | N | 0 |
| SproutLoud | — | — | — | — | — | — | 2 | G | N | 0 |
| Tidio | — | — | — | — | — | — | 2 | G | N | 0 |
| Touchdown | — | — | — | — | — | — | 2 | G | N | 0 |
| Trueblue | — | — | — | — | — | — | 2 | G | N | 0 |
| Voyado | — | — | — | — | — | — | 2 | G | N | 0 |
| Webmaxy | — | — | — | — | — | — | 2 | G | N | 0 |
| Webmecanik | — | — | — | — | — | — | 2 | G | N | 0 |
| ZEPIC | — | — | — | — | — | — | 2 | G | N | 0 |
| adnymics | — | — | — | — | — | — | 1 | G | N | 0 |
| AEvent | — | — | — | — | — | — | 1 | G | N | 0 |
| AfterShip | — | — | — | — | — | — | 1 | G | N | 0 |
| Agillic | — | — | — | — | — | — | 1 | G | N | 0 |
| Aislelabs | — | — | — | — | — | — | 1 | G | N | 0 |
| Alterian | — | — | — | — | — | — | 1 | G | N | 0 |
| Amazing Mail | — | — | — | — | — | — | 1 | G | N | 0 |
| Amazon Web Services | — | — | — | — | — | — | 1 | G | N | 0 |
| Appier | — | — | — | — | — | — | 1 | G | N | 0 |
| AT Internet | — | — | — | — | — | — | 1 | G | N | 0 |
| AtomPark Software | — | — | — | — | — | — | 1 | G | N | 0 |
| AWeber | — | — | — | — | — | — | 1 | G | N | 0 |
| Barilliance | — | — | — | — | — | — | 1 | G | N | 0 |
| Base | — | — | — | — | — | — | 1 | G | N | 0 |
| Beaconsmind | — | — | — | — | — | — | 1 | G | N | 0 |
| Benchmark Email | — | — | — | — | — | — | 1 | G | N | 0 |
| Birdeye | — | — | — | — | — | — | 1 | 2 | N | 0 |
| BiteSpeed | — | — | — | — | — | — | 1 | G | N | 0 |
| Blueshift | — | — | — | — | — | — | 1 | G | N | 0 |
| BrandOps | — | — | — | — | — | — | 1 | G | N | 0 |
| Bridgeline Digital | — | — | — | — | — | — | 1 | G | N | 0 |
| BSI Software | — | — | — | — | — | — | 1 | G | N | 0 |
| BUSINESSNEXT | — | — | — | — | — | — | 1 | G | N | 0 |
| CAKE | — | — | — | — | — | — | 1 | G | N | 0 |
| Campaigner | — | — | — | — | — | — | 1 | G | N | 0 |
| CentraHub | — | — | — | — | — | — | 1 | G | N | 0 |
| ChannelMix | — | — | — | — | — | — | 1 | G | N | 0 |
| ClickDimensions | — | — | — | — | — | — | 1 | G | N | 0 |
| Close | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Creatio | — | — | — | — | — | — | 1 | G | N | 0 |
| Critical Impact | — | — | — | — | — | — | 1 | G | N | 0 |
| CustomerInsights.ai | — | — | — | — | — | — | 1 | G | N | 0 |
| DANAconnect | — | — | — | — | — | — | 1 | G | N | 0 |
| Datorama | — | — | — | — | — | — | 1 | G | N | 0 |
| Delivra | — | — | — | — | — | — | 1 | G | N | 0 |
| Digitalbox | — | — | — | — | — | — | 1 | G | N | 0 |
| Duda | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Dyrect | — | — | — | — | — | — | 1 | G | N | 0 |
| Dyspatch | — | — | — | — | — | — | 1 | G | N | 0 |
| E-goi | — | — | — | — | — | — | 1 | G | N | 0 |
| Ecomail | — | — | — | — | — | — | 1 | G | N | 0 |
| EcoSend | — | — | — | — | — | — | 1 | G | N | 0 |
| Emailidea | — | — | — | — | — | — | 1 | G | N | 0 |
| Emma | — | — | — | — | — | — | 1 | 2 | N | 0 |
| EngageBay Inc | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Entirely | — | — | — | — | — | — | 1 | G | N | 0 |
| EZ Texting | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Flodesk | — | — | — | — | — | — | 1 | 2 | N | 0 |
| FlowUp | — | — | — | — | — | — | 1 | G | N | 0 |
| FollowAnalytics | — | — | — | — | — | — | 1 | G | N | 0 |
| Foursquare | — | — | — | — | — | — | 1 | G | N | 0 |
| Free Stand Sampling Solutions | — | — | — | — | — | — | 1 | G | N | 0 |
| Fresh Relevance | — | — | — | — | — | — | 1 | G | N | 0 |
| Freshworks | — | — | — | — | — | — | 1 | G | N | 0 |
| Frizbit | — | — | — | — | — | — | 1 | G | N | 0 |
| GetResponse | — | — | — | — | — | — | 1 | 2 | N | 0 |
| GMass | — | — | — | — | — | — | 1 | 2 | N | 0 |
| GoSquared | — | — | — | — | — | — | 1 | G | N | 0 |
| Grey Box | — | — | — | — | — | — | 1 | G | N | 0 |
| HCLTech | — | — | — | — | — | — | 1 | G | N | 0 |
| Health Chain | — | — | — | — | — | — | 1 | G | N | 0 |
| Hewlett Packard Enterprise | — | — | — | — | — | — | 1 | G | N | 0 |
| Hey Sid | — | — | — | — | — | — | 1 | G | N | 0 |
| HOLLYFY | — | — | — | — | — | — | 1 | G | N | 0 |
| Hostinger | — | — | — | — | — | — | 1 | G | N | 0 |
| IBM | — | — | — | — | — | — | 1 | G | N | 0 |
| iContact | — | — | — | — | — | — | 1 | G | N | 0 |
| InAppStory | — | — | — | — | — | — | 1 | G | N | 0 |
| Inflection.io | — | — | — | — | — | — | 1 | G | N | 0 |
| Insightly | — | — | — | — | — | — | 1 | G | N | 0 |
| Inspired Thinking Group | — | — | — | — | — | — | 1 | G | N | 0 |
| Instantly | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Intense Technologies | — | — | — | — | — | — | 1 | G | N | 0 |
| Iorta TechNxt | — | — | — | — | — | — | 1 | G | N | 0 |
| IQVIA | — | — | — | — | — | — | 1 | G | N | 0 |
| Kenyt.AI | — | — | — | — | — | — | 1 | G | N | 0 |
| L-Soft | — | — | — | — | — | — | 1 | G | N | 0 |
| Leadspicker | — | — | — | — | — | — | 1 | G | N | 0 |
| LeadSquared | — | — | — | — | — | — | 1 | G | N | 0 |
| LeadsRx | — | — | — | — | — | — | 1 | G | N | 0 |
| lemlist | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Levitate | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Lob | — | — | — | — | — | — | 1 | G | N | 0 |
| Longtail UX | — | — | — | — | — | — | 1 | G | N | 0 |
| Mailgun | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Mapp | — | — | — | — | — | — | 1 | G | N | 0 |
| Marigold | — | — | — | — | — | — | 1 | G | N | 0 |
| MarketingPlatform | — | — | — | — | — | — | 1 | G | N | 0 |
| Marketplacer | — | — | — | — | — | — | 1 | G | N | 0 |
| Mastercard | — | — | — | — | — | — | 1 | G | N | 0 |
| Medallia | — | — | — | — | — | — | 1 | G | N | 0 |
| Meiro | — | — | — | — | — | — | 1 | G | N | 0 |
| Mekari | — | — | — | — | — | — | 1 | G | N | 0 |
| Messangi | — | — | — | — | — | — | 1 | G | N | 0 |
| Metadata | — | — | — | — | — | — | 1 | G | N | 0 |
| MINT | — | — | — | — | — | — | 1 | G | N | 0 |
| MobiMesh | — | — | — | — | — | — | 1 | G | N | 0 |
| Mobivity | — | — | — | — | — | — | 1 | G | N | 0 |
| NerdMonster Digital Retail | — | — | — | — | — | — | 1 | G | N | 0 |
| OBASE | — | — | — | — | — | — | 1 | G | N | 0 |
| Ometria | — | — | — | — | — | — | 1 | G | N | 0 |
| ONLINECITY.IO | — | — | — | — | — | — | 1 | G | N | 0 |
| Ortto | — | — | — | — | — | — | 1 | G | N | 0 |
| PAR | — | — | — | — | — | — | 1 | G | N | 0 |
| Perion | — | — | — | — | — | — | 1 | G | N | 0 |
| Pitney Bowes | — | — | — | — | — | — | 1 | G | N | 0 |
| Piwik PRO | — | — | — | — | — | — | 1 | G | N | 0 |
| Podium | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Postal | — | — | — | — | — | — | 1 | G | N | 0 |
| Postalytics | — | — | — | — | — | — | 1 | G | N | 0 |
| PostcardMania | — | — | — | — | — | — | 1 | G | N | 0 |
| PostGrid | — | — | — | — | — | — | 1 | G | N | 0 |
| Precisely | — | — | legacy | — | — | — | 1 | G | N | 0 |
| Printfection | — | — | — | — | — | — | 1 | G | N | 0 |
| Pyze | — | — | — | — | — | — | 1 | G | N | 0 |
| Qujam | — | — | — | — | — | — | 1 | G | N | 0 |
| Radar | — | — | — | — | — | — | 1 | G | N | 0 |
| Reachdesk | — | — | — | — | — | — | 1 | G | N | 0 |
| Redpoint | — | — | — | — | — | — | 1 | G | N | 0 |
| Rejoiner | — | — | — | — | — | — | 1 | G | N | 0 |
| Resulticks | — | — | — | — | — | — | 1 | G | N | 0 |
| Reteno | — | — | — | — | — | — | 1 | G | N | 0 |
| Rocket Now | — | — | — | — | — | — | 1 | G | N | 0 |
| SALESmanago | — | — | — | — | — | — | 1 | G | N | 0 |
| SAS | — | — | legacy | — | — | — | 1 | G | N | 0 |
| Sendoso | — | — | — | — | — | — | 1 | G | N | 0 |
| SendPulse | — | — | — | — | — | — | 1 | G | N | 0 |
| Sensors Data | — | — | — | — | — | — | 1 | G | N | 0 |
| Sitecore | — | — | — | — | — | — | 1 | G | N | 0 |
| SlickText | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Soprano | — | — | — | — | — | — | 1 | G | N | 0 |
| Spectrm | — | — | — | — | — | — | 1 | G | N | 0 |
| SpiceSend | — | — | legacy | — | — | — | 1 | G | N | 0 |
| Splio | — | — | — | — | — | — | 1 | G | N | 0 |
| Sprinklr | — | — | — | — | — | — | 1 | G | N | 0 |
| Storyly | — | — | — | — | — | — | 1 | G | N | 0 |
| Striker Soft Solutions | — | — | — | — | — | — | 1 | G | N | 0 |
| SugarAI | — | — | — | — | — | — | 1 | G | N | 0 |
| SwiftERM Hyper-Personalisation | — | — | — | — | — | — | 1 | G | N | 0 |
| Swrve | — | — | — | — | — | — | 1 | G | N | 0 |
| Text | — | — | — | — | — | — | 1 | G | N | 0 |
| Textedly | — | — | — | — | — | — | 1 | 2 | N | 0 |
| Thryv | — | — | — | — | — | — | 1 | G | N | 0 |
| Treasure AI | — | — | — | — | — | — | 1 | G | N | 0 |
| Trendemon | — | — | — | — | — | — | 1 | G | N | 0 |
| Twilio | — | — | — | — | — | — | 1 | G | N | 0 |
| Upaknee | — | — | — | — | — | — | 1 | G | N | 0 |
| UTM.io | — | — | — | — | — | — | 1 | G | N | 0 |
| ValueFirst | — | — | — | — | — | — | 1 | G | N | 0 |
| Veloxy IO | — | — | — | — | — | — | 1 | G | N | 0 |
| VeryUtils | — | — | — | — | — | — | 1 | G | N | 0 |
| Vibes | — | — | — | — | — | — | 1 | G | N | 0 |
| Warmy | — | — | — | — | — | — | 1 | G | N | 0 |
| Webflow | — | — | — | — | — | — | 1 | 2 | N | 0 |
| WILY | — | — | — | — | — | — | 1 | G | N | 0 |
| Woosmap | — | — | — | — | — | — | 1 | G | N | 0 |
| WorksBuddy | — | — | — | — | — | — | 1 | G | N | 0 |
| xiQ | — | — | — | — | — | — | 1 | G | N | 0 |
| Yotpo | — | — | — | — | — | — | 1 | G | N | 0 |
