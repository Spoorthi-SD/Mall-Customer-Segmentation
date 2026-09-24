import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mall Customer Segmentation",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv("outputs/customer_segments.csv")


# ============================================================
# CUSTOMER GROUP INFORMATION
# ============================================================

cluster_names = {
    0: "Average Customers",
    1: "High-Value Customers",
    2: "High-Spending, Lower-Income",
    3: "High-Income, Low-Spending",
    4: "Low-Income, Low-Spending"
}

cluster_descriptions = {
    0: "Average income and average spending",
    1: "High income and high spending",
    2: "Lower income but high spending",
    3: "High income but low spending",
    4: "Lower income and low spending"
}

df["Segment"] = df["Cluster"].map(cluster_names)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #0a1220;
    color: #ffffff;
}


/* =========================================================
   REMOVE STREAMLIT TOP HEADER
   ========================================================= */

[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}


.block-container {
    max-width: 1700px;
    padding-top: 1.5rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    padding-bottom: 2rem;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    background-color: #101a2b;
    border-right: 1px solid #25344d;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

.sidebar-title {
    font-size: 22px;
    font-weight: 750;
    color: #ffffff;
    margin-top: 5px;
}

.sidebar-subtitle {
    font-size: 12px;
    color: #ffffff;
    margin-top: 3px;
    margin-bottom: 22px;
}


/* =========================================================
   REDUCE LARGE SIDEBAR SECTION SPACING
   ========================================================= */

[data-testid="stSidebar"] hr {
    margin-top: 0px !important;
    margin-bottom: 0px !important;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}

[data-testid="stSidebar"] .stMarkdown {
    margin-bottom: 0px !important;
}


/* =========================================================
   SIDEBAR RADIO HEADINGS
   ========================================================= */

[data-testid="stSidebar"] .stRadio [data-testid="stWidgetLabel"] p {
    font-size: 15px !important;
    font-weight: 600 !important;
}


/* =========================================================
   STREAMLIT METRICS
   ========================================================= */

[data-testid="stMetricLabel"] {
    color: #ffffff !important;
}

[data-testid="stMetricLabel"] p {
    color: #ffffff !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

[data-testid="stMetricValue"] div {
    color: #ffffff !important;
}

[data-testid="stMetricDelta"] {
    color: #ffffff !important;
}


/* =========================================================
   HEADER
   ========================================================= */

.dashboard-title {
    font-size: 34px;
    font-weight: 750;
    color: #ffffff;
    margin-bottom: 2px;
}

.dashboard-subtitle {
    color: #ffffff;
    font-size: 14px;
    margin-bottom: 22px;
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.metric-card {
    background: linear-gradient(
        145deg,
        #16243a,
        #101b2d
    );

    border: 1px solid #263852;
    border-radius: 13px;

    padding: 17px 20px;

    min-height: 105px;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.16);
}

.metric-label {
    color: #ffffff;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.metric-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 750;
    margin-top: 5px;
}

.metric-description {
    color: #ffffff;
    font-size: 11px;
    margin-top: 3px;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    color: #ffffff;
    font-size: 19px;
    font-weight: 700;
    margin-top: 22px;
    margin-bottom: 10px;
}


/* =========================================================
   CLUSTER CARDS
   ========================================================= */

.cluster-card {
    background-color: #111c2f;
    border: 1px solid #263852;
    border-radius: 11px;
    padding: 13px 12px;
    min-height: 145px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.13);
}

.cluster-number {
    color: #36b9cc;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.6px;
}

.cluster-name {
    color: #ffffff;
    font-size: 14px;
    font-weight: 650;
    line-height: 1.25;
    margin-top: 4px;
}

.cluster-description {
    color: #ffffff;
    font-size: 10px;
    line-height: 1.35;
    margin-top: 7px;
}

.cluster-stat {
    color: #ffffff;
    font-size: 10px;
    margin-top: 8px;
}

.cluster-stat strong {
    color: #ffffff;
}


/* =========================================================
   INSIGHT CARDS
   ========================================================= */

.insight-card {
    background-color: #111c2f;
    border: 1px solid #263852;
    border-radius: 11px;
    padding: 14px 16px;
    margin-bottom: 8px;
}

.insight-title {
    color: #ffffff;
    font-size: 14px;
    font-weight: 650;
}

.insight-text {
    color: #ffffff;
    font-size: 12px;
    line-height: 1.45;
    margin-top: 4px;
}


/* =========================================================
   DATAFRAME
   ========================================================= */

[data-testid="stDataFrame"] {
    border: 1px solid #263852;
    border-radius: 10px;
}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton > button {
    background-color: #0b84a5;
    color: #ffffff;
    border: none;
    border-radius: 7px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    color: #ffffff;
    font-size: 10px;
    padding-top: 15px;
    padding-bottom: 5px;
}


/* =========================================================
   DIVIDER
   ========================================================= */

hr {
    border-color: #24344c;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛍️ Mall Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Customer Segmentation Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### Dashboard")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Customer Explorer",
            "Cluster Profiles",
            "Model Insights"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### Filters")

    selected_cluster = st.radio(
        "Customer Group",
        ["All Groups"] + list(cluster_names.values()),
        index=0
    )

    selected_gender = st.radio(
        "Gender",
        ["All", "Female", "Male"],
        index=0
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

if selected_cluster != "All Groups":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_cluster
    ]

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">Mall Customer Segmentation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">Interactive customer analytics powered by K-Means clustering</div>',
    unsafe_allow_html=True
)


# ============================================================
# KPI SECTION
# ============================================================

total_customers = len(filtered_df)

avg_income = filtered_df["Annual Income (k$)"].mean()
avg_spending = filtered_df["Spending Score (1-100)"].mean()

k1, k2, k3, k4 = st.columns(4, gap="medium")


with k1:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">TOTAL CUSTOMERS</div>'
        f'<div class="metric-value">{total_customers}</div>'
        f'<div class="metric-description">Customers in selected view</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k2:

    st.markdown(
        '<div class="metric-card">'
        '<div class="metric-label">CUSTOMER GROUPS</div>'
        '<div class="metric-value">5</div>'
        '<div class="metric-description">K-Means clusters</div>'
        '</div>',
        unsafe_allow_html=True
    )


with k3:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">AVERAGE INCOME</div>'
        f'<div class="metric-value">${avg_income:.1f}k</div>'
        f'<div class="metric-description">Annual income</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k4:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">AVG. SPENDING SCORE</div>'
        f'<div class="metric-value">{avg_spending:.1f}</div>'
        f'<div class="metric-description">Out of 100</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "Overview":

    st.markdown(
        '<div class="section-title">Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # SCATTER PLOT
    # ========================================================

    fig = px.scatter(
        filtered_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color="Segment",
        hover_data=[
            "CustomerID",
            "Gender",
            "Age"
        ],
        template="plotly_dark"
    )

    fig.update_traces(
        marker=dict(
            size=10,
            line=dict(width=1)
        )
    )

    fig.update_layout(

        title=dict(
            text="Income vs Spending Score",
            font=dict(
                color="#ffffff",
                size=16
            )
        ),

        height=480,

        paper_bgcolor="#111c2f",
        plot_bgcolor="#111c2f",

        font=dict(
            family="Arial",
            color="#ffffff",
            size=12
        ),

        xaxis=dict(
            title=dict(
                text="Annual Income (k$)",
                font=dict(
                    color="#ffffff",
                    size=12
                )
            ),
            tickfont=dict(
                color="#ffffff",
                size=11
            ),
            gridcolor="#34445f",
            zerolinecolor="#34445f"
        ),

        yaxis=dict(
            title=dict(
                text="Spending Score (1-100)",
                font=dict(
                    color="#ffffff",
                    size=12
                )
            ),
            tickfont=dict(
                color="#ffffff",
                size=11
            ),
            gridcolor="#34445f",
            zerolinecolor="#34445f"
        ),

        legend=dict(
            title=dict(
                text="Customer Groups",
                font=dict(
                    color="#ffffff",
                    size=13
                )
            ),
            font=dict(
                color="#ffffff",
                size=12
            ),
            bgcolor="#111c2f",
            bordercolor="#263852",
            borderwidth=1
        ),

        margin=dict(
            l=25,
            r=25,
            t=55,
            b=25
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # CUSTOMER GROUPS
    # ========================================================

    st.markdown(
        '<div class="section-title">Customer Groups</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#ffffff;font-size:12px;margin-bottom:12px;">'
        'K-Means groups customers with similar income and spending behavior.'
        '</div>',
        unsafe_allow_html=True
    )

    cluster_columns = st.columns(5, gap="small")


    for cluster, column in enumerate(cluster_columns):

        segment_data = df[
            df["Cluster"] == cluster
        ]

        with column:

            card_html = (
                f'<div class="cluster-card">'
                f'<div class="cluster-number">CLUSTER {cluster}</div>'
                f'<div class="cluster-name">{cluster_names[cluster]}</div>'
                f'<div class="cluster-description">{cluster_descriptions[cluster]}</div>'
                f'<div class="cluster-stat">Customers: '
                f'<strong>{len(segment_data)}</strong></div>'
                f'<div class="cluster-stat">Income: '
                f'<strong>${segment_data["Annual Income (k$)"].mean():.1f}k</strong></div>'
                f'<div class="cluster-stat">Spending: '
                f'<strong>{segment_data["Spending Score (1-100)"].mean():.1f}</strong></div>'
                f'</div>'
            )

            st.markdown(
                card_html,
                unsafe_allow_html=True
            )


    # ========================================================
    # LOWER CHARTS
    # ========================================================

    c1, c2 = st.columns(2, gap="medium")


    # ========================================================
    # CUSTOMER DISTRIBUTION
    # ========================================================

    with c1:

        counts = (
            filtered_df["Segment"]
            .value_counts()
            .reset_index()
        )

        counts.columns = [
            "Segment",
            "Customers"
        ]

        fig = px.bar(
            counts,
            x="Segment",
            y="Customers",
            color="Segment",
            template="plotly_dark"
        )

        fig.update_layout(

            title=dict(
                text="Customer Distribution",
                font=dict(
                    color="#ffffff",
                    size=16
                )
            ),

            height=380,

            paper_bgcolor="#111c2f",
            plot_bgcolor="#111c2f",

            font=dict(
                family="Arial",
                color="#ffffff",
                size=12
            ),

            xaxis=dict(
                title=dict(
                    text="Customer Group",
                    font=dict(
                        color="#ffffff"
                    )
                ),
                tickfont=dict(
                    color="#ffffff"
                ),
                gridcolor="#34445f"
            ),

            yaxis=dict(
                title=dict(
                    text="Number of Customers",
                    font=dict(
                        color="#ffffff"
                    )
                ),
                tickfont=dict(
                    color="#ffffff"
                ),
                gridcolor="#34445f"
            ),

            showlegend=False,

            margin=dict(
                l=20,
                r=20,
                t=55,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # INCOME DISTRIBUTION
    # ========================================================

    with c2:

        fig = px.box(
            filtered_df,
            x="Segment",
            y="Annual Income (k$)",
            color="Segment",
            template="plotly_dark"
        )

        fig.update_layout(

            title=dict(
                text="Income Distribution",
                font=dict(
                    color="#ffffff",
                    size=16
                )
            ),

            height=380,

            paper_bgcolor="#111c2f",
            plot_bgcolor="#111c2f",

            font=dict(
                family="Arial",
                color="#ffffff",
                size=12
            ),

            xaxis=dict(
                title=dict(
                    text="Customer Group",
                    font=dict(
                        color="#ffffff"
                    )
                ),
                tickfont=dict(
                    color="#ffffff"
                ),
                gridcolor="#34445f"
            ),

            yaxis=dict(
                title=dict(
                    text="Annual Income (k$)",
                    font=dict(
                        color="#ffffff"
                    )
                ),
                tickfont=dict(
                    color="#ffffff"
                ),
                gridcolor="#34445f"
            ),

            showlegend=False,

            margin=dict(
                l=20,
                r=20,
                t=55,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif page == "Customer Explorer":

    st.markdown(
        '<div class="section-title">Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#ffffff;">'
        'Explore individual customer records using the filters in the sidebar.'
        '</div>',
        unsafe_allow_html=True
    )

    display_columns = [
        "CustomerID",
        "Gender",
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)",
        "Cluster",
        "Segment"
    ]

    st.dataframe(
        filtered_df[
            display_columns
        ].sort_values("CustomerID"),
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Selected Customer Statistics</div>',
        unsafe_allow_html=True
    )

    s1, s2, s3 = st.columns(3)


    with s1:

        st.metric(
            "Customers",
            len(filtered_df)
        )


    with s2:

        st.metric(
            "Average Age",
            f"{filtered_df['Age'].mean():.1f}"
        )


    with s3:

        st.metric(
            "Average Spending",
            f"{filtered_df['Spending Score (1-100)'].mean():.1f}"
        )


# ============================================================
# CLUSTER PROFILES
# ============================================================

elif page == "Cluster Profiles":

    st.markdown(
        '<div class="section-title">Cluster Profiles</div>',
        unsafe_allow_html=True
    )

    profile = (
        df.groupby(
            ["Cluster", "Segment"]
        )
        .agg(
            Customers=("CustomerID", "count"),
            Average_Income=(
                "Annual Income (k$)",
                "mean"
            ),
            Average_Spending=(
                "Spending Score (1-100)",
                "mean"
            )
        )
        .reset_index()
    )

    profile["Average_Income"] = (
        profile["Average_Income"].round(2)
    )

    profile["Average_Spending"] = (
        profile["Average_Spending"].round(2)
    )

    st.dataframe(
        profile,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Income and Spending Profile</div>',
        unsafe_allow_html=True
    )

    profile_long = profile.melt(
        id_vars=[
            "Cluster",
            "Segment"
        ],
        value_vars=[
            "Average_Income",
            "Average_Spending"
        ],
        var_name="Metric",
        value_name="Value"
    )

    profile_long["Metric"] = (
        profile_long["Metric"]
        .replace({
            "Average_Income": "Average Income",
            "Average_Spending": "Average Spending"
        })
    )

    fig = px.bar(
        profile_long,
        x="Segment",
        y="Value",
        color="Metric",
        barmode="group",
        template="plotly_dark"
    )

    fig.update_layout(

        title=dict(
            text="Average Income vs Spending Score",
            font=dict(
                color="#ffffff",
                size=16
            )
        ),

        height=500,

        paper_bgcolor="#111c2f",
        plot_bgcolor="#111c2f",

        font=dict(
            family="Arial",
            color="#ffffff",
            size=12
        ),

        xaxis=dict(
            title=dict(
                text="Customer Group",
                font=dict(
                    color="#ffffff"
                )
            ),
            tickfont=dict(
                color="#ffffff"
            ),
            gridcolor="#34445f"
        ),

        yaxis=dict(
            title=dict(
                text="Value",
                font=dict(
                    color="#ffffff"
                )
            ),
            tickfont=dict(
                color="#ffffff"
            ),
            gridcolor="#34445f"
        ),

        legend=dict(
            title=dict(
                text="Metric",
                font=dict(
                    color="#ffffff"
                )
            ),
            font=dict(
                color="#ffffff"
            ),
            bgcolor="#111c2f",
            bordercolor="#263852",
            borderwidth=1
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# MODEL INSIGHTS
# ============================================================

elif page == "Model Insights":

    st.markdown(
        '<div class="section-title">Model Insights</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)


    with m1:

        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-label">ALGORITHM</div>'
            '<div class="metric-value" style="font-size:22px;">K-Means</div>'
            '<div class="metric-description">Unsupervised learning</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with m2:

        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-label">CLUSTERS</div>'
            '<div class="metric-value">5</div>'
            '<div class="metric-description">Selected configuration</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with m3:

        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-label">SILHOUETTE SCORE</div>'
            '<div class="metric-value">0.5547</div>'
            '<div class="metric-description">Cluster quality measure</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # BUSINESS INSIGHTS
    # ========================================================

    st.markdown(
        '<div class="section-title">Business Insights</div>',
        unsafe_allow_html=True
    )

    insights = [
        (
            "High-Value Customers",
            "Cluster 1 contains high-income customers with high spending scores."
        ),
        (
            "High-Income, Low-Spending",
            "Cluster 3 contains customers with high income but relatively low spending scores."
        ),
        (
            "High-Spending, Lower-Income",
            "Cluster 2 contains customers with lower income but high spending scores."
        ),
        (
            "Low-Income, Low-Spending",
            "Cluster 4 contains customers with both lower income and lower spending scores."
        ),
        (
            "Average Customers",
            "Cluster 0 represents customers with moderate income and moderate spending."
        )
    ]

    for title, description in insights:

        insight_html = (
            f'<div class="insight-card">'
            f'<div class="insight-title">{title}</div>'
            f'<div class="insight-text">{description}</div>'
            f'</div>'
        )

        st.markdown(
            insight_html,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'Mall Customer Segmentation • K-Means Machine Learning Project'
    '<br>'
    'Built with Python, Scikit-learn, Pandas, Plotly and Streamlit'
    '</div>',
    unsafe_allow_html=True
)