# 🎮 Pokemon DynamoDB Collector

Pokemon collection application that uses AWS DynamoDB to store Pokemon data fetched from the PokeAPI.

## 📋 Overview

This application allows users to:
- Draw random Pokemon from the PokeAPI
- Store Pokemon data in AWS DynamoDB
- Retrieve and display Pokemon information from the database
- Automatic infrastructure deployment on AWS

## 🏗️ Architecture

```
User Input → Python App → PokeAPI (if new Pokemon)
                ↓
         AWS DynamoDB (Pokemon Storage)
                ↓
           Display Results
```

## 🛠️ Technologies Used

- **Python 3**: Main application language
- **AWS DynamoDB**: NoSQL database for Pokemon storage
- **PokeAPI**: Pokemon data source
- **boto3**: AWS SDK for Python
- **CloudFormation**: Infrastructure as Code

## 🚀 Quick Start

### Prerequisites

- AWS Account with appropriate permissions
- Python 3.7+

### Run the application:
```bash
pip install -r .\requirements.txt
python main.py
```

## 🎯 Usage

When you run the application:

1. You'll be prompted: "Would you like to draw a Pokemon? (yes/no)"
2. If you answer 'yes':
   - A random Pokemon is selected from PokeAPI
   - If it exists in DynamoDB, it displays the stored data
   - If it doesn't exist, it fetches from PokeAPI, saves to DynamoDB, then displays
3. If you answer 'no', the application exits with a farewell message

## 🔧 Configuration

### Environment Variables

- `AWS_DEFAULT_REGION`: AWS region (default: us-west-2)
- `POKEMON_TABLE_NAME`: DynamoDB table name (default: pokemon-collection)

### IAM Permissions Required

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:CreateTable",
                "dynamodb:DescribeTable",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/pokemon-collection"
        }
    ]
}

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied Errors**:
   - Ensure EC2 instance has proper IAM role with DynamoDB permissions
   - Check that the role is attached to the instance

2. **Table Creation Fails**:
   - Verify AWS credentials are properly configured
   - Check if table already exists with different configuration

3. **PokeAPI Connection Issues**:
   - Ensure EC2 instance has internet connectivity
   - Check security group allows outbound HTTPS traffic

4. **Application Won't Start**:
   - Verify Python 3 is installed: `python3 --version`
   - Check dependencies are installed: `pip3 list`