# Rolling upgrade checklist

- [ ] Snapshots green
- [ ] Disable shard allocation as required by version guide
- [ ] Upgrade nodes one-by-one, wait green/yellow per procedure
- [ ] Re-enable allocation
- [ ] Validate queries and ingest lag
