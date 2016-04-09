# koios
Database distribution platform
==intro==
You might see this as a Database Load balancer, one network connection to address multiple databases on multiple platforms.
Like Oracle Connection Manager, or pgpool, but for multiple platforms.
You migth see this as a Logical Database manager, same as LVM, but for databases instead of block devices.

This platform will help in
* managing multiple database platforms, 
* migrating between them, 
* benefitting from best-of-bread between RDBMS-es, 
* etc.

Of coarse 'cloud enabled applications' have these features (and more) built in their architecture, but legacy applications will certainly benefit from using Koios as the connection layer.

==koios==

===wikipedia===
In Greek mythology, Coeus (Ancient Greek: Κοῖος, Koios, "query, questioning") was one of the Titans, the giant sons and daughters of Uranus (Heaven) and Gaia (Earth). His equivalent in Latin poetry - though he scarcely makes an appearance in Roman mythology - was Polus, the embodiment of the celestial axis around which the heavens revolve. The etymology of Coeus' name provided several scholars the theory that Coeus was also the Titan god of intellect, who represented the inquisitive mind.

Like most of the Titans he played no active part in Greek religion—he appears only in lists of Titans—but was primarily important for his descendants. With his sister, "shining" Phoebe, Coeus fathered Leto and Asteria. Though it is not explicitly mentioned, Lelantos was implied to be a son of Coeus, or at least Leto's male counterpart. Leto copulated with Zeus (the son of fellow Titans Cronus and Rhea) and bore Artemis and Apollo.

Given that Phoebe symbolized prophetic wisdom just as Coeus represented rational intelligence, the couple may have possibly functioned together as the primal font of all knowledge in the cosmos. Along with the other Titans, Coeus was overthrown by Zeus and the other Olympians in the Titanomachy. Afterwards, he and all his brothers were imprisoned in Tartarus by Zeus. Coeus, later overcome with madness, broke free from his bonds and attempted to escape his imprisonment, but was repelled by Cerberus.

===this project===
you can use the koios platform as THE GATEWAY to all rational intelligence in yout IT infrastructure.
Koios aims at bringing together multiple relational (and maybe noSQL in future functionality) to a single interface. This means that the application has a single point of contact that presents itselve as one database, but is in fact constructed from multiple databases in the backend. The benefit of using Koios as the 'database presentation layer' might be one, or more of:
* transparency between multiple database platforms, 
* migrating between them,
* benefitting from best-of-bread between RDBMS-es,
* load balancing / HA
* etc.

Since koios is only a presentation layer and does not hold any data (other than metadata), multiple instances can run in parallel giving koios, which adds load balancing and HA functionality to the platform.
