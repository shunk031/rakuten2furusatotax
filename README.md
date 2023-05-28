# [`rakuten`](https://www.rakuten.co.jp/) to [`furusato-tax.jp`](https://www.furusato-tax.jp/)

[![CI](https://github.com/shunk031/rakuten2furusatotax/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/rakuten2furusatotax/actions/workflows/ci.yaml)

```shell
cp .env.sample .env
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
