# これはなに

cdklocalとLocalstackのデモ用のリポジトリです。

# 使い方

下記を準備してください

- docker, docker-compose プラグイン等
- cdklocal

```bash
docker compose up
# dockerが立ったら、別のターミナルから実行
cd cdk
cdklocal bootstrap
cdklocal deploy 
```
