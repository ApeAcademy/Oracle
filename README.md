# Oracle Project

A tutorial of how to build a simple Oracle contract in Vyper using the Coinbase signed price feed.

## Background

Oracles are a common piece of infrastructure in the Crypto world.
Oracles are basically providers of off-chain information,
such as the prices of assets (crypto or otherwise), the occurence of specific events,
and basically any other piece of information that doesn't exist
solely within a smart contract in a blockchain environment.

Oracles are called by that name due to what is known as the
["Oracle Problem"](https://blog.chain.link/what-is-the-blockchain-oracle-problem/),
basically that it is impossible to know external information with absolutely certainty.
Further, there are a lot of other concerns with how information is integrated into the
blockchain's environment including what is the source of the information, what is it's
accuracy, how reliable are the updates during times of network stress (e.g. high fees),
how many parties control the updates to the information, and many more.

Bad Oracle designs have in the past led to huge hacks of blockchain systems.
This makes sense, because if you are relying on certain information to be accurate,
and the accuracy and/or timeliness of that information becomes an issue, certain
assumptions that the users of that information may have had would be impacted,
to catastrophic effect.

This tutorial isn't meant to be a perfectly complete project that will solve all these
problems from the start, but we highlight a simple design of this type of contract to
learn more about the fundamentals of Oracle contracts and how they operate.

## Specification

We are going to design a very simple contract that let's a user do two basic things:
1. Read an ETH/USD price feed that updates on a regular basis
2. Determine the accuracy of that information
