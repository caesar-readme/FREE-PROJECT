import secrets

class Game:
    def __init__(self):
        self.choices = ['telunjuk', 'kelingking', 'jempol']

    def play(self):
        while True:
            computer = secrets.choice(self.choices)

            player = input('Telunjuk, Kelingking, atau Jempol? Ketik "stop" jika ingin menghentikan permainan: ').lower()

            if player == 'stop':
                print('Permainan selesai. Terima kasih sudah bermain!')
                break

            if player in self.choices:
                if computer == player:
                    print(f"Komputer memilih '{computer}' dan Player memilih '{player}', hasilnya seri!")
                elif (player == 'telunjuk' and computer == 'kelingking') or (player == 'kelingking' and computer == 'jempol') or (player == 'jempol' and computer == 'telunjuk'):
                    print(f"Komputer memilih '{computer}' dan Player memilih '{player}', hasilnya Player menang!")
                else:
                    print(f"Komputer memilih '{computer}' dan Player memilih '{player}', hasilnya Komputer menang!")
            else:
                print("Tolong masukkan pilihan yang sesuai!")
                break

            play_again = input('Main lagi? (yes/no): ').lower()

            if play_again != 'yes':
                break

        print('Permainan selesai. Terima kasih sudah bermain!')


game = Game()
game.play()
