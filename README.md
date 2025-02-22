# Traffic Forecasting - PhD Research
Repository for my PhD thesis on Traffic Forecasting.

## Citation
To cite this work in your publications, please use the following BibTeX entry:

```
@phdthesis{Esugo2023HybridEnvironments,
  title = {{Hybrid Deep-Learning Models and Evaluation Methods for Short-Term Traffic Flow Forecasting}},
  year = {2023},
  author = {Esugo, Martin},
  school = {Coventry University}
}
```
## Abstract
Urban centres worldwide are increasingly seeking efficient and reliable transportation systems to accommodate their growth. Traffic forecasting is a critical component of smart urban mobility strategies, providing the basis for efficient traffic control measures that can reduce congestion, minimise pollution, and improve journey times. However, the task of forecasting traffic is fraught with challenges due to the heterogeneous and cyclic nature of traffic data. Despite significant progress in the field, challenges remain in developing models that can consistently forecast a variety of traffic scenarios, selecting key input features for traffic forecasting, and establishing reliable metrics for evaluating model performance.

To address these challenges, this thesis introduces a Multi-Input Hybrid Deep Self-Attention Network (MIHDSAN) for short-term traffic forecasting. Unlike conventional models, MIHDSAN recognises the importance of weekly traffic periodicity as a key input feature, significantly enhancing its predictive accuracy in diverse traffic scenarios. This novel approach also incorporates a global self-attention mechanism, which not only improves the model's interpretability but also allows it to adaptively focus on the most relevant features in the traffic data. Furthermore, this thesis proposes new tunable loss and evaluation metric formulations based on the Geoffrey E. Havers (GEH) statistic, a well-established evaluation metric in traffic modelling. These novelties are specifically designed to overcome some of the limitations of existing models in handling the heterogeneous and cyclic nature of traffic data, thereby offering a more robust and accurate traffic forecasting model.

The MIHDSAN model and the new GEH-based metrics were evaluated using two independent traffic datasets. The results demonstrate that the inclusion of weekly traffic periodicity improved the model's performance by approximately 3\%. Moreover, the GEH-based loss and evaluation functions proved to be more consistent and reliable than the commonly used Mean Absolute Error (MAE) and Mean Squared Error (MSE) metrics. These findings suggest that the proposed GEH-based loss and evaluation functions could be adopted as standard criteria within the traffic forecasting community, potentially leading to more accurate and reliable traffic forecasting and, consequently, improved traffic management strategies.
