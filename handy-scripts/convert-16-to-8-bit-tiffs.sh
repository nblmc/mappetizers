for f in *.tif; do
convert $f -depth 8 $f-8bit.tif;
done
