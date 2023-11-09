import wget
#download do resultado da petrobras
link="https://api.mziq.com/mzfilemanager/v2/d/25fdf098-34f5-4608-b7fa-17d60b2de47d/77c83abf-faf4-1162-6e2e-24fcdda4dd5b?origin=1"

wget.download(link, "Resultado_petrobras.pdf")