# Setup and Configuration Guide

## 📋 Prerequisites

- n8n installed and running
- Python 3.7+ (for testing)
- Telegram Bot Token
- Chat ID for notifications

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-sensor-monitoring.git
   cd smart-sensor-monitoring
   ```

2. **Set up n8n**
   - Open n8n in your browser (default: http://localhost:5678)
   - Import `smart-sensor-workflow.json`
   - Configure your Telegram bot credentials
   - Update the chat ID in the "Send a text message" node

3. **Run tests (optional)**
   ```bash
   pip install -r requirements.txt
   python -m pytest
   ```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

### Threshold Configuration
Edit the "Check Parameters" node in n8n to adjust:
- Temperature threshold (default: 50°C)
- Gas level threshold (default: 0.5)

### Notification Settings
Modify the message template in the "Send a text message" node to customize alerts.

## 🧪 Testing

### Manual Testing
Run the test script:
```bash
python test_sensor.py
```

### Automated Tests
Run all tests:
```bash
pytest
```

## 🔄 Deployment

### n8n Cloud
1. Sign up at [n8n.cloud](https://www.n8n.cloud/)
2. Import the workflow
3. Set up environment variables
4. Activate the workflow

### Self-hosted
1. Install n8n using Docker:
   ```bash
   docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -v ~/.n8n:/home/node/.n8n \
     n8nio/n8n
   ```
2. Import the workflow
3. Set up environment variables
4. Start the workflow

## 📊 Monitoring

Check the n8n execution logs to monitor the workflow:
- Successful executions
- Failed executions
- Error messages
- Performance metrics

## 🔒 Security

- Keep your Telegram bot token and chat ID secure
- Use environment variables for sensitive data
- Regularly update n8n to the latest version
- Monitor execution logs for suspicious activity
