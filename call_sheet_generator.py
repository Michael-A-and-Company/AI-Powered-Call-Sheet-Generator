import pandas as pd
import random

# Sample donor data (you would replace this with your actual data)
donors_data = {
    'Donor Name': ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob Johnson', 'Charlie White'],
    'Last Donation Amount': [500, 150, 300, 1000, 250],
    'Donation History': [10, 5, 8, 20, 3],  # Number of previous donations
    'Engagement Score': [80, 55, 60, 95, 40],  # Score based on engagement with previous campaigns
}

# Convert data to DataFrame
df_donors = pd.DataFrame(donors_data)

# Function to calculate donor priority score
def calculate_priority(row):
    # Priority could be a weighted sum of the donation history and engagement score
    return (row['Donation History'] * 0.7) + (row['Engagement Score'] * 0.3)

# Apply the priority calculation to each donor
df_donors['Priority Score'] = df_donors.apply(calculate_priority, axis=1)

# Sort donors by their priority score (highest to lowest)
df_donors = df_donors.sort_values(by='Priority Score', ascending=False)

# Function to create a personalized call script for each donor
def create_call_script(row):
    # Personalized message based on donation amount and history
    return f"Hello {row['Donor Name']},\n\nThank you for your generous contribution of ${row['Last Donation Amount']}! We truly appreciate your ongoing support and would love to discuss how your continued involvement can make a big impact in this election. You’ve donated {row['Donation History']} times before, and we’d love to see if you can increase your support this year.\n\nBest regards,\nYour Campaign Team"

# Apply the call script generation to each donor
df_donors['Call Script'] = df_donors.apply(create_call_script, axis=1)

# Create a final call sheet
call_sheet = df_donors[['Donor Name', 'Last Donation Amount', 'Priority Score', 'Call Script']]

# Output the call sheet
def output_call_sheet(call_sheet):
    print("Call Sheet for Political Fundraising Campaign\n")
    print("Donor Name | Last Donation | Priority Score | Call Script\n")
    for _, row in call_sheet.iterrows():
        print(f"\n{row['Donor Name']} | ${row['Last Donation Amount']} | {row['Priority Score']} | \n{row['Call Script']}")

# Run the output function
output_call_sheet(call_sheet)