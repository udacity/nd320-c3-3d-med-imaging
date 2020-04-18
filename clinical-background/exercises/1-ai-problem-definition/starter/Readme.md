# Lesson 1 Exercise

## Choosing a clinical problem and framing it as a machine learning task

So far you have heard from a clinician about some of the opportunities in medical imaging for AI tools. You have seen some examples of medical imaging problems ripe for disruption, and you have been introduced to the concept of medical imaging modalities and the many clinical specialties that deal with medical imaging.

We will dive deeper into many of these topics, including imaging formats and some machine learning algorithms for image processing, but for now we would like you to start thinking about clinical problems from AI engineer perspective.

In this exercise we want you to practice how to choose a clinical problem to tackle, explore how to research some basic facts about the disease, and frame the clinical problem as a machine learning task. You will not be expected to write code in this exercise. Rather, you will write a project proposal as a free form document. Don't be daunted - you are the best judge of this proposal, so write one that you think you will be able to show to a fellow clinician.

## Part 1: Choosing a clinical case

Exciting clinical problems abound in the realm of Healthcare AI. To help you narrow down some potential ideas, we will use the American College of Radiology Data Science Institute (ACR DSI) curated list of use cases that is available by following [this link](https://www.acrdsi.org/DSI-Services/Define-AI). Alternatively, you may explore any clinical problem of your choosing without using the database if you already had something in mind. Please note that some use cases in the ACR DSI database can seem overwhelming or obscure without some background medical knowledge. If this is case, simply choose something that's more intuitive. A few good starting examples include: [Acute Appendicitis](https://www.acrdsi.org/DSI-Services/Define-AI/Use-Cases/Acute-Appendicitis), [Aging Brain - Dementia](https://www.acrdsi.org/DSI-Services/Define-AI/Use-Cases/Aging-Brain---Dementia), and [Incidental Pulmonary Nodules on CT](https://www.acrdsi.org/DSI-Services/Define-AI/Use-Cases/Incidental-Pulmonary-Nodules-on-CT).

Your task for this first part is to choose a case. If you choose to use the ACR DSI database, include **the link that points to your use case**. If using any other resources, please include an **image capture of PDF of a medical or AI journal article** that explores this problem within the context of machine learning.

## Part 2: Background research

To deliver an algorithm that performs well in a clinical setting, it can be extremely beneficial to have some rudimentary understanding of the disease or situation you are addressing. To do so, engaging in some background research to build your foundation will be crucial. For this part of the exercise, find a review article describing the problem. A good source of such articles is the PubMed database which is the initiative of the National Institutes of Health and contains over 30 million citations and full texts of biomedical articles and essays. PubMed database can be accessed here: https://pubmed.ncbi.nlm.nih.gov/

Ask yourself, "what is the current gold standard for confirming or ruling out the presence of this disease/state?". Understanding the current gold standard/ground truth test will be a critical benchmark when testing any algorithm you develop. In your project proposal, include a **screen capture or a PDF of the article**.

## Part 3: Framing the problem as a machine learning task

With some background knowledge of the disease or condition at hand, as well as how it is currently ruled in or out, consider how the task could be framed as a machine learning problem. We will be going over this in much more detail in further lessons of this course, but some early exposure will be useful. For example, solving the problem of autonomously detecting one or more lung nodules could be framed as an object detection task. Measuring changes in tumor volume over time may be best framed as a segmentation task, etc. Add a **short paragraph detailing how you would frame your clinical problem of choice as a machine learning task**, and explain your rationale.
