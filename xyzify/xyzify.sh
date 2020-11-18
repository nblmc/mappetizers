while read -r line
do
	echo "Beginning processing of $line"
	mkdir ./$line
	echo "Downloading $line tiles from S3"
	s3cmd get --recursive s3://urbanatlases/$line/tiles/ ./$line
	echo "Deleting extraneous files"
	cd ./$line
	find . -type f -size -335c -delete
	cd ../
	echo "Converting to XYZ"
	python3 tms-to-xyz.py $line
	echo "Deleting TMS tiles from S3"
	s3cmd del --recursive s3://urbanatlases/$line/tiles/
	echo "Uploading XYZ tiles from S3"
	cd ./$line
	for i in {13..20}
	do
		cd $i
		for f in *
		do
			s3cmd put --recursive $f s3://urbanatlases/$line/tiles/$i/
		done
		cd ../
	done
	cd ../
	echo "Deleting files locally"
	rm -rf ./$line
done < barcodes.txt