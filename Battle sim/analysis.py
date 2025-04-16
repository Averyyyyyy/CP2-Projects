# Avery bowman

import pandas as pd
import numpy as np
import os
import csv
from character import Character

def load_characters_to_dataframe():
    # Load characters from CSV into a Pandas DataFrame
    if not os.path.exists('characters.csv'):
        return pd.DataFrame()
    
    try:
        # Read CSV data
        df = pd.read_csv('characters.csv', header=None, 
                         names=['Name', 'Health', 'Strength', 'Defense', 'Speed', 'Level', 'Experience'])
        
        # Convert numeric columns
        numeric_cols = ['Health', 'Strength', 'Defense', 'Speed', 'Level', 'Experience']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col])
            
        return df
    except Exception as e:
        print(f"Error loading characters into DataFrame: {e}")
        return pd.DataFrame()

def get_character_stats(characters=None):
    # Calculate basic statistics for character attributes
    if characters is None:
        df = load_characters_to_dataframe()
    else:
        # Create DataFrame from list of Character objects
        data = []
        for char in characters:
            data.append([
                char.name,
                char.health,
                char.strength,
                char.defense,
                char.speed,
                char.level,
                char.experience
            ])
        
        df = pd.DataFrame(data, columns=['Name', 'Health', 'Strength', 'Defense', 'Speed', 'Level', 'Experience'])
    
    # Return empty stats if no data
    if df.empty:
        return {}
    
    # Calculate statistics (excluding Name column)
    numeric_cols = ['Health', 'Strength', 'Defense', 'Speed', 'Level', 'Experience']
    stats = {}
    
    for col in numeric_cols:
        if col in df.columns:
            stats[col] = {
                'mean': df[col].mean(),
                'median': df[col].median(),
                'min': df[col].min(),
                'max': df[col].max(),
                'std': df[col].std()
            }
    
    # Additional derived statistics
    if 'Health' in df.columns and 'Defense' in df.columns:
        df['Survivability'] = df['Health'] * (1 + df['Defense'] * 0.1)
        stats['Survivability'] = {
            'mean': df['Survivability'].mean(),
            'median': df['Survivability'].median(),
            'min': df['Survivability'].min(),
            'max': df['Survivability'].max(),
            'std': df['Survivability'].std()
        }
    
    if 'Strength' in df.columns and 'Speed' in df.columns:
        df['Attack_Power'] = df['Strength'] * (1 + df['Speed'] * 0.05)
        stats['Attack_Power'] = {
            'mean': df['Attack_Power'].mean(),
            'median': df['Attack_Power'].median(),
            'min': df['Attack_Power'].min(),
            'max': df['Attack_Power'].max(),
            'std': df['Attack_Power'].std()
        }
    
    return stats

def get_character_ranking(characters):
    # Rank characters based on their overall power
    if not characters:
        return []
    
    # Create a DataFrame with character data
    data = []
    for char in characters:
        # Calculate power score (custom formula)
        power_score = (
            char.health * 0.3 + 
            char.strength * 0.25 + 
            char.defense * 0.2 + 
            char.speed * 0.15 + 
            char.level * 10
        )
        
        data.append({
            'Name': char.name,
            'Level': char.level,
            'Health': char.health,
            'Strength': char.strength,
            'Defense': char.defense,
            'Speed': char.speed,
            'Power_Score': power_score
        })
    
    # Create DataFrame and sort by power score
    df = pd.DataFrame(data)
    ranked_chars = df.sort_values('Power_Score', ascending=False)
    
    return ranked_chars

def find_best_matchups(characters):
    # Find balanced matchups for battles
    if len(characters) < 2:
        return []
    
    # Create a DataFrame with character data
    data = []
    for char in characters:
        # Calculate power score (custom formula)
        power_score = (
            char.health * 0.3 + 
            char.strength * 0.25 + 
            char.defense * 0.2 + 
            char.speed * 0.15 + 
            char.level * 10
        )
        
        data.append({
            'Name': char.name,
            'Level': char.level,
            'Power_Score': power_score,
            'Character': char  # Store reference to character object
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Find matchups with similar power levels
    matchups = []
    for i, row1 in df.iterrows():
        for j, row2 in df.iterrows():
            if i < j:  # Only compare each pair once
                char1 = row1['Character']
                char2 = row2['Character']
                
                # Calculate power difference percentage
                power_diff = abs(row1['Power_Score'] - row2['Power_Score'])
                avg_power = (row1['Power_Score'] + row2['Power_Score']) / 2
                power_diff_pct = (power_diff / avg_power) * 100
                
                matchups.append({
                    'character1': char1,
                    'character2': char2,
                    'power_diff_pct': power_diff_pct
                })
    
    # Sort by closest power levels (smallest difference)
    matchups_sorted = sorted(matchups, key=lambda x: x['power_diff_pct'])
    
    return matchups_sorted

def analyze_stat_correlation(characters):
    # Find correlations between character attributes
    if len(characters) < 3:  # Need at least 3 characters for meaningful correlation
        return None
    
    # Create DataFrame from character data
    data = []
    for char in characters:
        data.append({
            'Name': char.name,
            'Health': char.health,
            'Strength': char.strength, 
            'Defense': char.defense,
            'Speed': char.speed,
            'Level': char.level
        })
    
    df = pd.DataFrame(data)
    
    # Calculate correlations between attributes
    # Exclude non-numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    
    return correlation_matrix

def export_character_stats(characters, filename='character_stats.csv'):
    # Export character stats to a CSV file
    if not characters:
        return False
    
    # Create DataFrame from character data
    data = []
    for char in characters:
        # Calculate derived stats
        survivability = char.health * (1 + char.defense * 0.1)
        attack_power = char.strength * (1 + char.speed * 0.05)
        
        data.append({
            'Name': char.name,
            'Level': char.level,
            'Health': char.health,
            'Strength': char.strength, 
            'Defense': char.defense,
            'Speed': char.speed,
            'Experience': char.experience,
            'Exp_To_Next': char.exp_to_level,
            'Survivability': survivability,
            'Attack_Power': attack_power
        })
    
    df = pd.DataFrame(data)
    
    # Export to CSV
    try:
        df.to_csv(filename, index=False)
        return True
    except Exception as e:
        print(f"Error exporting character stats: {e}")
        return False