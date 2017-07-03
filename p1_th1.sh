#!/bin/bash

NRNIV="../../../neuron_kplus/specials/x86_64/special -mpi"
HOC_NAME="./network.hoc"

NRNOPT=\
" -c OUT1_E=0.001"\
" -c OUT1_I=0.003"\
" -c IO_E=0.001"\
" -c IO_I2E=0.0001"\
" -c IO_I2I=0.0001"\
" -c OUT1_SPON_E_K=0.25"\
" -c OUT1_SPON_E_T=0.35"\
" -c DOPAMINE=0.02"\
" -c LEARNING_RATE=0.00025"\
" -c OUT1_SPON_I_K=0.25"\
" -c OUT1_SPON_I_T=0.3"\
" -c LTD=0.8"

MPIEXEC="mpiexec -mca mpi_print_stats 1"

#OUTPUT_FILE="../log/r$(date +%Y%m%d%H%M%S).log"

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
#echo $EXEC > ${OUTPUT_FILE}
echo $EXEC
time $EXEC

#gprof ${NRNIV} ./gmon.out >> ${OUTPUT_FILE}

#echo "OUTPUT_FILE = ${OUTPUT_FILE}"

sync


