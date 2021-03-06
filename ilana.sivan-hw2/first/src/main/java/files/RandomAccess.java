package files;

import java.io.IOException;
import java.io.RandomAccessFile;

public class RandomAccess {
    /**
     * Treat the file as an array of (unsigned) 8-bit values and sort them
     * in-place using a bubble-sort algorithm.
     * You may not read the whole file into memory!
     *
     * @param file
     */

    public static void sortBytes(RandomAccessFile file) throws IOException {

        int n = (int) file.length();

        for (int i = 0; i < n - 1; ++i) {
            for (int j = 0; j < n - 1; ++j) {
                file.seek(j);
                int a = file.read();

                file.seek(j + 1);
                int b = file.read();

                if (a > b) {
                    file.seek(j);
                    file.write(b);
                    file.seek(j + 1);
                    file.write(a);
                }
            }
        }
    }

    /**
     * Treat the file as an array of unsigned 24-bit values (stored MSB first) and sort
     * them in-place using a bubble-sort algorithm.
     * You may not read the whole file into memory!
     *
     * @param file
     * @throws IOException
     */
    public static void sortTriBytes(RandomAccessFile file) throws IOException {

        long a = 0, b = 0;
        long n = file.length() / 3;

        // bubbleSort again??
        for (long i = 0; i < n - 1; i++) {
            for (long j = 0; j < n - i - 1; j++) {

                // reads tribytes a and b
                a = convert2Tri(file, j * 3);
                b = convert2Tri(file, (j + 1) * 3);
                if (a > b) {

                    // swap
                    for (long k = 0; k < 3; k++) {
                        swap(file, (j * 3) + k, (j * 3) + k + 3);
                    }
                }
            }
        }
    }

    /**
     * The method swaps bytes by position
     *
     * @param file - the random access file to modify.
     * @param aPos -  position of  first byte.
     * @param bPos -  position of  second byte.
     * @throws IOException
     */
    public static void swap(RandomAccessFile file, long aPos, long bPos) throws IOException {

        // initialize
        int a, b;

        // save first byte
        file.seek(aPos);
        a = file.read();

        // and second
        file.seek(bPos);
        b = file.read();

        // swap
        file.seek(aPos);
        file.writeByte(b);

        file.seek(bPos);
        file.writeByte(a);
    }

    /**
     * The method takes a random access file and a position and converts the 3 following bytes to a tribyte.
     * The method returns the tribyte as a long.
     *
     * @param file - the random access file to read from.
     * @param pos - the position of the first byte in the tribyte.
     * @return long myNum
     * @throws IOException
     */
    public static long convert2Tri(RandomAccessFile file, long pos) throws IOException {

        file.seek(pos);

        Long myNum = (long) file.read() << 16;
        myNum |= (long) ((file.read()) << 8);
        myNum |= (long) ((file.read()));

        return myNum;
    }
}
