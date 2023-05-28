# [`rakuten`](https://www.rakuten.co.jp/) to [`furusato-tax.jp`](https://www.furusato-tax.jp/)

```shell
export $(cat .env| grep -v "#" | xargs)
```

```shell
rakuten2furusatotax \
    --rakuten-login-id ${RAKUTEN_LOGIN_ID} \
    --rakuten-password ${RAKUTEN_PASSWORD} \
    --furusato-tax-login-id ${FURUSATO_TAX_LOGIN_ID} \
    --furusato-tax-password ${FURUSATO_TAX_PASSWORD} \
    --disable-headless
```
