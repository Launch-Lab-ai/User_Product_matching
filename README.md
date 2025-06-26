## User_Product_matching
User preference scoring and matching system that predicts which product categories users are likely to prefer based on demographic data, then matches users to products in those categories.

## Overview
Predicts user preferences for product categories ("buckets") based on demographic data. It scores users for Fashion, Tech, Home & Decor, and Budget buckets, then matches top users with products categorized by Team B (product metadata).

## Features
- Calculates a likeability score (0–5) per user for each product bucket
- Matches products to the top 3 users likely to prefer them
- Outputs user scores and product-user matches as CSV files

## Data
- User data: Train.csv (from Kaggle dataset)
- Product data: flipkart_buckets_single_label.csv (from Team B)

(Can replace with another product dataset if needed)

## Output Files
user_bucket_scores.csv: User IDs and their scores for each bucket

product_user_matches.csv: Product info and the top 3 matched users with their scores

## Data Files Required
- `Train.csv`: Included in the repo
- `flipkart_buckets_single_label.csv`: **Not included**
Get from data in Product Metadata
