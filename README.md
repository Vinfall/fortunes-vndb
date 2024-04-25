# Fortunes-VNDB

Fortune file of VNDB quotes. Automatically updated through GitHub Action.

## Why

Quoted from Yorhel via [t1052.3](https://vndb.org/t1052.3):

> [!note]
> It takes all the fun of the randomness away if you know all of them already. :-P

And `fortunes` program has exactly the same charm.
It becomes somehow hilarious if you pass the quote to other programs like `cowsay`:

```sh
fortunes | cowsay
```

## Usage

0. Note that it may contain NSFW content or **spoilers** so use it at your own risk
1. Install `fortune-mod` or `fortunes` from your package manager
2. Copy `vndb` AND `vndb.dat` to `/usr/share/fortunes` (or `/usr/share/games/fortunes`)
3. You can now have VNDB quote via `fortune vndb`

Example commands:

```sh
$ sudo cp ./vndb* /usr/share/fortunes/

$ fortune vndb
I spent all of last year's Shiomi Festival participating in a self-sponsored Reading Festival at my apartment, actually.
        -- 筧 京太郎, Daitoshokan no Hitsujikai (https://vndb.org/v8158)
```

## How

Data is obtained through [VNDB Query](https://query.vndb.org/schema#vndb.quotes).
I have no idea about the meaning of `score` so omit it on purpose.

PostgreSQL Query:

```sql
SELECT vid, cid, quote
FROM vndb.quotes;
```

Or query VN titles, character names and format the output altogether:

```sql
SELECT
  q.quote,
  CASE
    WHEN c.name IS NULL THEN CONCAT (v.title, ' (https://vndb.org/' || q.vid || ')')
    ELSE CONCAT (c.name, ', ', v.title, ' (https://vndb.org/' || q.vid || ')')
  END AS source
FROM
  quotes q
  JOIN vn v ON q.vid = v.id
  LEFT JOIN chars c ON q.cid = c.id
```

If you want to create a custom VNDB fortune quote, you can either edit coded SQL query in [`format.py`](format.py) on VNDB Query,
or alternatively, run the script locally, edit the JSON, and make a fortune dat yourself.

## [License](LICENSE)

- Fortunes-VNDB is released into Public Domain under [The Unlicense](https://unlicense.org).
- [Query](https://query.vndb.org/5c9a6037d875c238) inspired by
  - [All quotes on the DB (optional filter by VN)](https://query.vndb.org/6d95933cb5acd0d6)
  - [Quotes and their games](https://query.vndb.org/6d55820399bae5ef)
- [Data License](https://vndb.org/d17#4)
  - All information on VNDB is made available under the [Open Database License](https://opendatacommons.org/licenses/odbl/1.0/).
  - Any rights in individual contents of the database are licensed under the [Database Contents License](https://opendatacommons.org/licenses/dbcl/1.0/).
