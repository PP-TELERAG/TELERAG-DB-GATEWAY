# TELERAG-DB-GATEWAY
Gateway for Mongo DB manipulations
## Features

- Simplified MongoDB operations.
- Secure and efficient database gateway.
- Scalable and easy to integrate.

## Installation

### Production
```bash
git clone https://github.com/your-repo/TELERAG-DB-GATEWAY.git
cd TELERAG-DB-GATEWAY
```

Change enviroments variables

```bash
docker compose up -d
```

### Development

```bash
git clone https://github.com/your-repo/TELERAG-DB-GATEWAY.git
cd TELERAG-DB-GATEWAY
```

Change enviroments variables

```bash
cat env_sample > .env
```

Create Python virtual enviroment
```bash
python3 -m venv venv
```
Activate
```bash
source venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Run development server
```bash
python3 -m fastapi dev src/main.py
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.
6. Bla bla bla and other information that no one will read

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.