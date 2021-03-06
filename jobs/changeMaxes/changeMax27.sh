#!/bin/bash -x
#
#PJM --rsc-list "rscgrp=small"
#PJM --rsc-list "node=124"
#PJM --rsc-list "elapse=01:00:00"
#PJM --mpi "proc=992"
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

#PJM --stgin "rank=* ./* %r:./"
#PJM --stgin "rank=* ./data/* %r:./data/"
#PJM --stgin "rank=* ./weights/* %r:./weights/"
#PJM --stgin "rank=* ./result/* %r:./result/"
#PJM --stgin "rank=* ./change/* %r:./change/"

#PJM --stgin "rank=* /home/hp120263/k01792/neuron_kplus/stgin/* %r:./"
#PJM --stgin "rank=* /home/hp120263/k01792/neuron_kplus/specials/sparc64/special %r:./"

#PJM --stgout "rank=* %r:./result/* /data/hp120263/fukuda/multi_sw2times/result/%j/"
#PJM --stgout "rank=* %r:./change/* /data/hp120263/fukuda/multi_sw2times/change/%j/"

#PJM -s
#PJM -m "e"
#PJM --mail-list "fukuda@brain.imi.i.u-tokyo.ac.jp"
#

. /work/system/Env_base

#NRNIV="../../../neuron_kplus/specials/sparc64/special -mpi"
NRNIV="./special -mpi"
HOC_NAME="./network.hoc"

NRNOPT=\
" -c OUT1_E=0.01"\
" -c OUT1_I=0.03"\
" -c IO_E=0.02"\
" -c IO_I2E=0.3"\
" -c IO_I2I=0.0005"\
" -c OUT1_SPON_E_K=0.15"\
" -c OUT1_SPON_E_T=0.35"\
" -c DOPAMINE=0.05"\
" -c LEARNING_RATE=0.025"\
" -c OUT1_SPON_I_K=0.15"\
" -c OUT1_SPON_I_T=0.3"\
" -c LTD=1.0"\
" -c MAXWEIGHT=10"


LPG="lpgparm -t 4MB -s 4MB -d 4MB -p 4MB"
MPIEXEC="mpiexec -mca mpi_print_stats 1"
PROF=""
echo "${PROF} ${MPIEXEC} ${LPG} ${NRNIV} ${HOC_NAME}"
time ${PROG} ${MPIEXEC} ${LPG} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync