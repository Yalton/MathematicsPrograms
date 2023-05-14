from Quaternions import Quaternion



if __name__ == "__main__":
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(5, 6, 7, 8)
    print("q1:", q1)
    print("q2:", q2)
    print("q1 + q2:", q1 + q2)
    print("q1 - q2:", q1 - q2)
    print("q1 * q2:", q1 * q2)
    print("Conjugate of q1:", q1.conjugate())
    print("Norm of q1:", q1.norm())
    print("Inverse of q1:", q1.inverse())
