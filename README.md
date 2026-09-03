\# bb84-sim



A Python simulator of the BB84 quantum key distribution protocol.



Alice and Bob establish a shared secret key over a quantum channel. When Eve

performs an intercept-resend attack, the quantum bit error rate (QBER) of the

sifted key rises to \~25% instead of \~0%, which makes eavesdropping detectable.



\*\*Status:\*\* work in progress. Implemented so far: Alice's random bit and basis

generation.



\## Install



```

git clone https://github.com/<user>/bb84-sim.git

cd bb84-sim

python -m venv .venv

.venv\\Scripts\\activate

pip install -e ".\[dev]"

```



\## Tests



```

pytest

```



\## License



MIT — see \[LICENSE](LICENSE).



\## Citation



A DOI will be issued through Zenodo.

