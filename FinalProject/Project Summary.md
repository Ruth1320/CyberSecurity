**<u>Full Project Summary – Imaged-based phishing</u>**
**project movie is in the end**

In this project, we designed and implemented an image-based phishing
detection system using website screenshot images. The motivation behind
focusing on visual phishing is that many modern phishing attacks rely
less on textual content and more on deceptive user interface design.
Attackers often create fake login pages that closely imitate legitimate
websites, making screenshot-based detection an important complementary
approach to traditional NLP-based email filtering.

A key part of our work was dataset preparation. Since phishing
screenshots are not always available in structured formats, we organized
the dataset into two clear categories: benign screenshots and phishing
screenshots. We generated labeled CSV files containing relative file
paths and binary labels, allowing the dataset to be portable and
reproducible across different environments. We also applied a stratified
train/validation/test split to ensure that class distributions remain
consistent across all subsets, which is essential for fair evaluation
and preventing biased performance estimates.

Before modeling, we performed exploratory data analysis (EDA) to better
understand the dataset characteristics. This included analyzing class
balance, inspecting sample images, and examining image resolution
distributions. EDA is a crucial step in cybersecurity machine learning
because dataset artifacts or imbalance can lead to misleading results if
not addressed early.

For the baseline model, we selected ResNet18, a well-known convolutional
neural network architecture. Although ResNet18 is not the newest deep
learning model, it remains widely used in both academic research and
industry because it provides strong classification performance while
being computationally lightweight. This was especially important given
our hardware constraints, as the project was designed to run on a
standard CPU-based machine without requiring high-end GPUs.

To further improve efficiency, we applied transfer learning rather than
training a deep network from scratch. Specifically, we froze the
pretrained backbone layers and fine-tuned only the final classification
head (model.fc). This strategy allows the model to reuse general-purpose
visual features learned from ImageNet while adapting to
phishing-specific patterns with minimal computational cost. Fine-tuning
only the head also reduces the risk of overfitting, which is common when
working with limited cybersecurity datasets.

Because phishing datasets may be imbalanced, we incorporated weighted
cross-entropy loss to ensure that the minority class is not ignored
during training. This is a common best practice in security
classification tasks where false negatives (missed phishing cases) can
have serious consequences.

Beyond standard modeling, we implemented a structured pipeline inspired
by NVIDIA Morpheus. Although we did not deploy the full Morpheus
platform, we simulated its modular detection workflow: preprocessing,
inference, fingerprinting, decision logic, and result reporting. This
pipeline-based approach reflects real-world SOC systems, where detection
models are part of a larger automated flow that produces actionable
security decisions such as allowing or blocking suspicious content.

For evaluation, we reported standard classification metrics including
accuracy, precision, recall, F1-score, and confusion matrices. These
metrics provide a more complete understanding of model behavior than
accuracy alone, especially in security contexts where false positives
and false negatives have different operational costs.

Finally, we conducted basic robustness testing by applying simple
perturbations such as blur and brightness changes. This simulates how
attackers may attempt evasion through visual modifications or
compression artifacts, highlighting potential vulnerabilities of
image-based classifiers.  
results:  
Accuracy: 0.7215686274509804

Precision: 0.5533980582524272

Recall: 0.6951219512195121

F1: 0.6162162162162163

Confusion Matrix:

\[\[127 46\]

\[ 25 57\]\]

Results conclusion:  
The model does not collapse under this type of attack simulation.  
Even with distorted images, it still manages to detect a large portion
of phishing attempts, which demonstrates a certain level of robustness.
Of course, we could improve performance further by training longer,
using stronger augmentation, or fine-tuning more layers, but given the
CPU  
limitations and only two epochs, these results are still quite
encouraging.

Overall, our project demonstrates a realistic baseline for phishing
screenshot detection, combining practical dataset engineering, efficient
transfer learning, structured pipeline design, and security-focused
evaluation.

[Watch the project video](https://www.youtube.com/watch?v=n6HmBvUTTF4)
