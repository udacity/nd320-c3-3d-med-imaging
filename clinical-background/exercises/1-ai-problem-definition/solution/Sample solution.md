# Lesson 1 Exercise – Sample Solution 

## Part 1: Choosing a clinical case.

https://www.acrdsi.org/DSI-Services/Define-AI/Use-Cases/COVID-19-Compatible-Chest-CT-Pattern	

## Part 2: Background research.

https://pubs.rsna.org/doi/10.1148/radiol.2020200823

## Part 3: Framing the problem as a machine learning task.

Per the ACR-DSI, the assigned task is to provide a likelihood of a diagnosis compatible with COVID-19 using chest CT data. I believe an initial step in solving this clinical problem, determining whether any abnormal findings are present on a chest CT, would be well-framed as an object detection task. The output would be a bounding box delineating the areas of abnormality that could indicate viral pneumonia. Based on recent literature, such findings could include consolidation, bilateral and peripheral disease, linear opacities, “crazy-paving” pattern and the “reverse halo” sign. While these findings are not-specific for COVID-19, their detection could guide the ordering clinician to be more vigilant in follow-up testing for the disease. A negative STAT rapid influenza/RSV PCR tests and positive Real-Time Reverse Transcriptase Polymerase Chain Reaction (rRT-PCR) would confirm the diagnosis.
