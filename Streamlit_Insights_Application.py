import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv('cleaned_reports_data.csv')

# Set the title and description of the app
st.title('Streamlit Insights Application')
st.write('Explore various insights from the cleaned reports data.')

# Show the dataframe
if st.checkbox('Show raw data'):
    st.write(df)

# Display some basic information about the data
st.subheader('Basic Information')
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.write("Data types:")
st.write(df.dtypes)

# Plot Report Type Distribution
st.subheader('Report Type Distribution')
report_type_counts = df['report_type'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(report_type_counts.index, report_type_counts.values, color='skyblue')
ax.set_xlabel('Report Type', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Report Type Distribution', fontsize=14)
st.pyplot(fig)

# Insights from Report Type Distribution
st.write("**Insight**: The distribution of reports by type shows the most common types of reports created in the system. "
         "It helps to identify that PowerBI Reports most frequently created by users.")

# Temporal Trends - Reports Created Over Time
st.subheader('Reports Created Over Time')
df['created_date_time'] = pd.to_datetime(df['created_date_time'], errors='coerce')
df['month_created'] = df['created_date_time'].dt.to_period('M')
monthly_report_creation = df['month_created'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_report_creation.index.astype(str), monthly_report_creation.values, marker='o', color='coral')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Reports', fontsize=12)
ax.set_title('Reports Created Over Time', fontsize=14)
plt.xticks(rotation=90)
st.pyplot(fig)

# Insights from Temporal Trends
st.write("**Insight**: The temporal trend shows how the number of reports created varies over time. "
         "This can help in understanding the trends and seasonal patterns in report creation, "
         "which might be tied to specific events or activities."
         " Here maximum report are created in August 2022 and July 2023.")

# User Activity - Frequency of Report Modifications by Each User
st.subheader('User Activity - Frequency of Report Modifications')
user_activity = df['modified_by'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(user_activity.index, user_activity.values, color='salmon')
ax.set_xlabel('User', fontsize=12)
ax.set_ylabel('Number of Reports Modified', fontsize=12)
ax.set_title('User Activity - Frequency of Report Modifications', fontsize=14)
plt.xticks(rotation=90)
st.pyplot(fig)

# Insights from User Activity
st.write("**Insight**: The frequency of report modifications by each user highlights how active users are in modifying reports. "
         "It can help identify users who are most engaged with the report modification process."
         " Most of the reports are modified by unknown user who user ID is not mentioned.")

# Report Type Distribution Across Workspaces
st.subheader('Report Type Distribution Across Workspaces')
workspace_report_type_distribution = df.groupby('workspace_name')['report_type'].value_counts().unstack()
st.write(workspace_report_type_distribution)

# Insights from Workspace Report Distribution
st.write("**Insight**: The report type distribution across workspaces gives a detailed look at how different workspaces generate "
         "various types of reports. This can provide insights into workspace-specific reporting trends.")

# Report Type Distribution Across Users (Heatmap)
st.subheader('Report Type Distribution Across Users (Heatmap)')
user_report_type_distribution = df.groupby('modified_by')['report_type'].value_counts().unstack().fillna(0)
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(user_report_type_distribution, annot=True, cmap='YlGnBu', fmt='g', cbar_kws={'label': 'Number of Reports'}, ax=ax)
ax.set_title("Report Type Distribution Across Users (Heatmap)", fontsize=16)
st.pyplot(fig)

# Insights from Report Type Distribution Across Users (Heatmap)
st.write("**Insight**: The heatmap shows how users interact with different report types. It helps in understanding which users are "
         "modifying particular types of reports and can provide insight into user preferences and engagement with report types.")

# Analyzing the number of reports generated per workspace
st.subheader('Workspace Usage - Number of Reports per Workspace')
workspace_usage = df['workspace_name'].value_counts()
fig, ax = plt.subplots(figsize=(12, 6))
workspace_usage.plot(kind='bar', color='skyblue', ax=ax)
ax.set_xlabel('Workspace', fontsize=12)
ax.set_ylabel('Number of Reports', fontsize=12)
ax.set_title('Workspace Usage - Number of Reports per Workspace', fontsize=14)
st.pyplot(fig)

# Insights from Workspace Usage
st.write("**Insight**: This analysis helps in understanding the number of reports generated across different workspaces. "
         "It could highlight which workspaces are more active or have a higher number of reports generated."
         " Transportation has the highest number of reports."
         )

# Analyzing the number of reports stored on dedicated capacity vs general storage
st.subheader('Storage Distribution - Dedicated Capacity vs General Storage')
storage_distribution = df['is_on_dedicated_capacity'].value_counts()
st.write(storage_distribution)
fig, ax = plt.subplots(figsize=(8, 6))
storage_distribution.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'], startangle=90, ax=ax)
ax.set_title('Storage Distribution - Dedicated Capacity vs General Storage', fontsize=14)
st.pyplot(fig)

# Insights from Storage Distribution
st.write("**Insight**: This pie chart shows the proportion of reports stored on dedicated capacity vs general storage. "
         "It helps understand how the reports are distributed in terms of storage infrastructure.")

# Plot Domain Report Distribution
st.subheader('Report Distribution per Domain')
domain_report_distribution = df['domain_id'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(domain_report_distribution.index, domain_report_distribution.values, color='lightgreen')
ax.set_xlabel('Domain ID', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Report Distribution per Domain', fontsize=14)
st.pyplot(fig)

# Insights from Domain Report Distribution
st.write("**Insight**: The report distribution across domains indicates the areas or categories where most reports are being generated. "
         "We can see that maximum domain is unknown which can be concerning to know the exact user of it.")