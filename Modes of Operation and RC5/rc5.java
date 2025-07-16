public class RC5 {
    private static final int WORD_SIZE = 32;
    private static final int R = 12;
    private static final int B = 8;
    private static final int C = B / 4;
    private static final int T = 2 * (R + 1);

    private int[] S = new int[T];
    private static final int P = 0xb7e15163;
    private static final int Q = 0x9e3779b9;

    public RC5(byte[] key) {
        keySchedule(key);
    }

    private void keySchedule(byte[] key) {
        int[] L = new int[C];
        for (int i = 0; i < B; i++) {
            L[i / 4] = (L[i / 4] << 8) | (key[i] & 0xFF);
        }

        S[0] = P;
        for (int i = 1; i < T; i++) {
            S[i] = S[i - 1] + Q;
        }

        int A = 0, B = 0, i = 0, j = 0;
        for (int k = 0; k < 3 * T; k++) {
            A = S[i] = Integer.rotateLeft(S[i] + A + B, 3);
            B = L[j] = Integer.rotateLeft(L[j] + A + B, (A + B) % WORD_SIZE);
            i = (i + 1) % T;
            j = (j + 1) % C;
        }
    }

    private int[] encrypt(int[] pt) {
        int A = pt[0] + S[0];
        int B = pt[1] + S[1];

        for (int i = 1; i <= R; i++) {
            A = Integer.rotateLeft(A ^ B, B % WORD_SIZE) + S[2 * i];
            B = Integer.rotateLeft(B ^ A, A % WORD_SIZE) + S[2 * i + 1];
        }

        return new int[]{A, B};
    }

    public int[] decrypt(int[] ct) {
        int B = ct[1];
        int A = ct[0];
        for (int i = R; i >= 1; i--) {
            B = Integer.rotateRight(B - S[2 * i + 1], A % WORD_SIZE) ^ A;
            A = Integer.rotateRight(A - S[2 * i], B % WORD_SIZE) ^ B;
        }
        A -= S[0];
        B -= S[1];
        return new int[]{A, B};
    }

    public static void main(String[] args) {
        byte[] key = "password".getBytes();
        RC5 rc5 = new RC5(key);

        int[] plaintext = {0x12345678, 0x9abcdef0};
        int[] ciphertext = rc5.encrypt(plaintext);

        System.out.printf("Ciphertext: %08x %08x%n", ciphertext[0], ciphertext[1]);

        int[] decrypted = rc5.decrypt(ciphertext);
        System.out.printf("Decrypted: %08x %08x%n", decrypted[0], decrypted[1]);
    }
}

PS D:\4th Year 1st Semester\ICT-4105 Cryptography and Cyber Law\Modes of Operation and RC5> 
Ciphertext: 70e77036 27731364
Decrypted: 12345678 9abcdef0