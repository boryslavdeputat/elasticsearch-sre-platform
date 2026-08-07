# Shard strategy

- Target shard size 20-50 GB (search) depending on heap and use case
- primary shards fixed at index create - plan growth
- Avoid oversharding small indices
- Force-merge only on read-only indices
- Watch cluster state size and master stability
