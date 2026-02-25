# Fortunes-VNDB

Fortune file of VNDB quotes. Automatically updated through GitHub Action.

## Why

Quoted from Yorhel via [t1052.3][t1052.3]:

> [!note]
> It takes all the fun of the randomness away if you know all of them already. :-P

And `fortunes` program has exactly the same charm.
It becomes somehow hilarious if you pass the quote to other programs like `cowsay`:

```sh
fortunes | cowsay
```

## Usage

> [!TIP]
> It may contain NSFW content or **spoilers** so use it at your own risk!

1. Install `fortune-mod` or `fortunes` from your package manager
2. Copy [`vndb`][vndb] AND [`vndb.dat`][vndb.dat] to `/usr/share/fortunes` (or `/usr/share/games/fortunes`)
3. Get random VNDB quote via `fortune vndb`

Example commands:

```sh
# download fortunes
wget https://github.com/Vinfall/fortunes-vndb/releases/download/continuous/vndb{,.dat}
# install
# replace "/usr/share/fortunes/" with "/usr/share/games/fortunes/" if needed
sudo install -pm644 ./vndb* /usr/share/fortunes/

$ fortune vndb
I spent all of last year's Shiomi Festival participating in a self-sponsored Reading Festival at my apartment, actually.
        -- 筧 京太郎, Daitoshokan no Hitsujikai (https://vndb.org/v8158)
```

## How

Data is obtained through [VNDB Query][vndb-query].
I have no idea about the meaning of `score` so omit it on purpose.

PostgreSQL Query:

```sql
SELECT vid, cid, quote
FROM vndb.quotes;
```

Or query VN titles, character names and format the output altogether, check [`query.sql`](query.sql).

If you want to create a custom VNDB fortune quote, you can either edit coded SQL query in [`format.py`](format.py) on VNDB Query,
or alternatively, run the script locally, edit the JSON, and make a fortune dat yourself.

## [License](LICENSE)

- Fortunes-VNDB is released into Public Domain under [The Unlicense][unlicense].
- Query inspired by
  - [All quotes on the DB (optional filter by VN)][query-1]
  - [Quotes and their games][query-2]
- [Data License][license]
  - All information on VNDB is made available under the [Open Database License][ODBL].
  - Any rights in individual contents of the database are licensed under the [Database Contents License][DBCL].

[t1052.3]: https://vndb.org/t1052.3
[vndb]: https://github.com/Vinfall/fortunes-vndb/releases/download/continuous/vndb
[vndb.dat]: https://github.com/Vinfall/fortunes-vndb/releases/download/continuous/vndb.dat
[vndb-query]: https://query.vndb.org/schema#vndb.quotes
[unlicense]: https://unlicense.org
[query-1]: https://query.vndb.org/6d95933cb5acd0d6
[query-2]: https://query.vndb.org/6d55820399bae5ef
[license]: https://vndb.org/d17#4
[ODBL]: https://opendatacommons.org/licenses/odbl/1.0/
[DBCL]: https://opendatacommons.org/licenses/dbcl/1.0/
