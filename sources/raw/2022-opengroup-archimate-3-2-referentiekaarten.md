® 

# **ArchiMate**<sup>**®**</sup> **3.2 Specification** 

**Reference Cards** 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification** 

|**ArchiMate**<sup>**®**</sup>**3.2 Specification**<br>**Relationships and Relationship Connectors**|®|
|---|---|
|**Structural Relationships**|**Notation**|
|Composition<br>Represents that an element consists of one or more other concepts.||
|Aggregation<br>Represents that an element combines one or more other concepts.||
|Assignment<br>Represents the allocation of responsibility, performance of behavior,<br>storage,or execution.||
|Realization<br>Represents that an element plays a critical role in the creation,<br>achievement,sustenance,or operation of a more abstract element.||
|**Dependency Relationships**|**Notation**|
|Serving<br>Represents that an element provides its functionality to another<br>element.||
|Access<br>Represents the ability of behavior and active structure elements to<br>observe or act upon passive structure elements.||
|Influence<br>Represents that an element affects the implementation or achievement<br>of some motivation element.|+/-|
|Association<br>Respesents an unspecified relationship, or one that is not represented<br>byanother ArchiMate relationship.||
|**Dynamic Relationships**|**Notation**|
|Triggering<br>Represents a temporal or causal relationship between elements.||
|Flow<br>Represents transfer from one element to another.||
|**Other Relationships**|**Notation**|
|Specialization<br>Represents that an element is a particular kind of another element.||
|<br>**Relationship Connectors**|**Notation**|
|Junction<br>Used to connect relationships of the same type.|��������������<br>�����������|



### **Relationships and Relationship Connectors** 

N221 Personal PDF Edition 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Motivation Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Stakeholder|Represents the role of an individual, team, or organization<br>(or classes thereof) that represents their interests in the<br>effects of the architecture.|Stakeholder|
|Driver|Represents an external or internal condition that motivates<br>an organization to define its goals and implement the<br>changes necessary to achieve them.|Driver|
|Assessment|Represents the result of an analysis of the state of affairs<br>of the enterprise with respect to some driver.|Assessment|
|Goal|Represents a high-level statement of intent, direction, or<br>desired end state for an organization and its stakeholders.|Goal|
|Outcome|Represents an end result, effect, or consequence of a<br>certain state of affairs.|Outcome|





<!-- Start of picture text -->
G oa l<br>Outco<br>me<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Motivation Elements – continued** 

|**ArchiMate**<sup>**®**</sup>**i**<br>**Motivation E**|**3.2 Specification**<br>**lements – continued**|®|
|---|---|---|
|**Element**|**�efinition**|**Notation**|
|Principle|Represents a statement of intent defining a general<br>property that applies to any system in a certain context in<br>the architecture.|Principle|
|Requirement|Represents a statement of need defining a property<br>that applies to a specific system as described by the<br>architecture.|Requirement|
|Constraint|Represents a limitation on aspects of the architecture, its<br>implementation process, or its realization.|Constraint|
|Meaning|Represents the knowledge or expertise present in, or the<br>interpretation given to, a concept in a particular context.|Meaning|
|Value|Represents the relative worth, utility, or importance of a<br>concept.|Value|



N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Strategy Layer Elements** 

|**ArchiMate**<sup>**®**</sup>**3 i**<br>**Strategy Laye**|**.2 Specification**<br>**r Elements**|®|
|---|---|---|
|**Element**|**�efinition**|**Notation**|
|Resource|Represents an asset owned or controlled by an individual<br>or organization.|Resource|
|Capability|Represents an ability that an active structure element, such<br>as an organization, person, or system, possesses.|Capability|
|Value Stream|Represents a sequence of activities that create an overall<br>result for a customer, stakeholder, or end user.|Value<br>Stream|
|Course of Action|Represents an approach or plan for configuring some<br>capabilities and resources of the enterprise, undertaken to<br>achieve a goal.|Course of<br>Action|





<!-- Start of picture text -->
Value Stream<br>Course of Action<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Business Layer Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Business Actor|Represents a business entity that is capable of performing<br>behavior.|Business<br>Actor|
|Business Role|Represents the responsibility for performing specific<br>behavior, to which an actor can be assigned, or the part an<br>actor plays in a particular action or event.|Business<br>Role|
|Business<br>Collaboration|Represents an aggregate of two or more business internal<br>active structure elements that work together to perform<br>collective behavior.|Business<br>Collaboration|
|Business Interface|Represents a point of access where a business service is<br>made available to the environment.|Business<br>Interface|
|Business Process|Represents a sequence of business behaviors that<br>achieves a specific result such as a defined set of products<br>or business services.|Business<br>Process|
|Business Function|Represents a collection of business behavior based on a<br>chosen set of criteria (typically required business resources<br>and/or competencies), closely aligned to an organization,<br>but not necessarily explicitly governed bythe organization.|Business<br>Function|





<!-- Start of picture text -->
Business Role<br>Business Collaboration<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Business Layer Elements – continued** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Business<br>Interaction|Represents a unit of collective business behavior performed<br>by (a collaboration of) two or more business actors, business<br>roles, or business collaborations.|Business<br>Interaction|
|Business Event|Represents a business-related state change.|Business<br>Event|
|Business Service|Represents explicitly defined behavior that a business role,<br>business actor, or business collaboration exposes to its<br>environment.|Business<br>Service|
|Business Object|Represents a concept used within a particular business<br>domain.|Business<br>Object|
|Contract|Represents a formal or informal specification of an agreement<br>between a provider and a consumer that specifies the rights<br>and obligations associated with a product and establishes<br>functional and non-functionalparameters for interaction.|Contract|
|Representation|Represents a perceptible form of the information carried by a<br>business object.|Representation|
|Product|Represents a coherent collection of services and/or passive<br>structure elements, accompanied by a contract, which is<br>offered as a whole to (internal or external) customers.|Product|





<!-- Start of picture text -->
Business Service<br>Business Object<br><!-- End of picture text -->

N221 Personal PDF Edition 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Application Layer Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**||**Notation**|
|---|---|---|---|
|Application<br>Component|Represents an encapsulation of application functionality<br>aligned to implementation structure, which is modular and<br>replaceable.|Application<br>Component||
|Application<br>Collaboration|Represents an aggregate of two or more application internal<br>active structure elements that work together to perform<br>collective application behavior.|Application<br>Collaboration||
|Application<br>Interface|Represents a point of access where application services are<br>made available to a user, another application component, or a<br>node.|Application<br>Interface||
|Application<br>Function|Represents automated behavior that can be performed by an<br>application component.|Application<br>Function||
|Application<br>Interaction|Represents a unit of collective application behavior performed<br>by (a collaboration of) two or more application components.|Application<br>Interaction||
|Application Process|Represents a sequence of application behaviors that achieves<br>a specific result.|Application<br>Process||
|Application Event|Represents an application state change.|Application<br>Event||
|Application Service|Represents an explicitly defined exposed application behavior.|Application<br>Service||
|Data Object|Represents data structured for automated processing.|Data Object||





<!-- Start of picture text -->
Application Interface<br>Application Function<br>Application Interaction<br>Application Process<br>Application Event<br>Application Service<br>Data Object<br><!-- End of picture text -->

N221 Personal PDF Edition 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Technology Layer Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Node|Represents a computational or physical resource that hosts,<br>manipulates, or interacts with other computational or physical<br>resources.|Node|
|Device|Represents a physical IT resource upon which system software<br>and artifacts may be stored or deployed for execution.|Device|
|System Software|Represents software that provides or contributes to an<br>environment for storing, executing, and using software or data<br>deployed within it.|System<br>Software|
|Technology<br>Collaboration|Represents an aggregate of two or more technology internal<br>active structure elements that work together to perform collective<br>technology behavior.|Technology<br>Collaboration|
|Technology Interface|Represents a point of access where technology services<br>offered by a technology internal active structure element can be<br>accessed.|Technology<br>Interface|
|Path|Represents a link between two or more technology internal active<br>structure elements, through which these elements can exchange<br>data, energy, or material.|Path|
|Communication<br>Network|Represents a set of structures and behaviors that connects<br>devices or system software for transmission, routing, and<br>reception of data.|Communication<br>Network|





<!-- Start of picture text -->
Device<br>System Software<br><!-- End of picture text -->



<!-- Start of picture text -->
Technology Collaboration<br>Technology Interface<br><!-- End of picture text -->



<!-- Start of picture text -->
Path<br>Communication Network<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Technology Layer Elements – continued** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Technology<br>Function|Represents a collection of technology behavior that can<br>be performed by a technology internal active structure<br>element.|Technology<br>Function|
|Technology<br>Process|Represents a sequence of technology behaviors that<br>achieves a specific result.|Technology<br>Process|
|Technology<br>Interaction|Represents a unit of collective technology behavior<br>performed by (a collaboration of) two or more technology<br>internal active structure elements.|Technology<br>Interaction|
|Technology Event|Represents a technology state change.|Technology<br>Event|
|Technology<br>Service|Represents an explicitly defined exposed technology<br>behavior.|Technology<br>Service|
|Artifact|Represents a piece of data that is used or produced in<br>a software development process, or by deployment and<br>operation of an IT system.|Artifact|





<!-- Start of picture text -->
Technology Process<br>Technology Interaction<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification** 

### **Technology Layer Elements – continued** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->



<!-- Start of picture text -->
Element �ef i nition Notation<br>Equipment Represents one or more physical machines, tools, or<br>instruments that can create, use, store, move, or transform  Equipment<br>Equipment<br>materials.<br>Facility Represents a physical structure or environment.<br>Facility Facility<br>Distribution  Represents a physical network used to transport materials<br>Network or energy. Distribution<br>Network Distribution Network<br>Material Represents tangible physical matter or energy.<br>Material Material<br><!-- End of picture text -->

N221 Personal PDF Edition 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Implementation and Migration Layer Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->

|**Element**|**�efinition**|**Notation**|
|---|---|---|
|Work Package|Represents a series of actions identified and designed to<br>achieve specific results within specified time and resource<br>constraints.|Work<br>Package|
|Deliverable|Represents a precisely defined result of a work package.|Deliverable|
|Implementation<br>Event|Represents a state change related to implementation or<br>migration.|Implementation<br>Event|
|Plateau|Represents a relatively stable state of the architecture that<br>exists during a limited period of time.|Plateau|
|Gap|Represents a statement of difference between two<br>plateaus.|<br>Gap|



N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 

## **ArchiMate**<sup>**®**</sup> **3.2 Specification Composite Elements** 



<!-- Start of picture text -->
®<br><!-- End of picture text -->



<!-- Start of picture text -->
Element �ef i nition Notation<br>Grouping The grouping element aggregates or composes concepts that<br>belong together based on some common characteristic.<br>Grouping Grouping<br>Location A location represents a conceptual or physical place or<br>position where concepts are located (e.g., structure elements)  Location<br>or performed (e.g., behavior elements).<br>Location<br><!-- End of picture text -->

N221 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. 

Personal PDF Edition 



#### **_About The Open Group_** 

**Leading the development of open, vendor-neutral IT standards and ce�tification�** 

The Open Group is a global consortium that enables the achievement of business objectives through technology standards. With more than 870 member organizations, we have a diverse membership that spans all sectors of the technology community – customers, systems and solutions suppliers, tool vendors, integrators and consultants, as well as academics and researchers. 

##### **Keys facts include:** 

- Over 870 Member organizations, with 43,000+ participants in The Open Group activities from 126 countries 

- Our Platinum Members are DXC Technology, Fujitsu, HCL, Huawei, IBM, Intel, Micro Focus, and Philips 

- Services provided include strategy, management, innovation and research, standards, certification, and test development. 

- Over 120,000 TOGAF<sup>®</sup> Certifications worldwide 

Further information on The Open Group can be found at www.opengroup.org . 

Copyright © 2022 The Open Group. All Rights Reserved. ArchiMate<sup>®</sup> is a registered trademark of The Open Group. Personal PDF Edition 

