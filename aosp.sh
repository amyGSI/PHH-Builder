mkdir aosp
cd aosp
repo init -u https://android.googlesource.com/platform/manifest -b android-10.0.0_r31
git clone https://github.com/phhusson/treble_manifest -b android-10.0 .repo/local_manifests
repo sync -j128
. build/envsetup.sh
lunch treble_a64_bvS-userdebug
make -j9 systemimage
lunch treble_a64_avS-userdebug
make -j9 systemimage
