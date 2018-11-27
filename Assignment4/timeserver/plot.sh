#!/usr/bin/env bash


gnuplot <<- EOF
	set title "Time server status over time"
	set xlabel "Unix Time"
	set ylabel "RPS (1-minute rate)"
	set autoscale
	set term png
	set output "result.png"
	plot 'comp.txt' using 1:2 title '500s' with lines,\
	'comp.txt' using 1:3 title '200s' with lines,\
	'comp.txt' using 1:4 title '404s' with lines
EOF
rm comp.txt