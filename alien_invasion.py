import sys
from time import sleep

import pygame

from setting import Setting
from game_stats import GameStats
from button import Button
from ship import Ship

from bullet import Bullet

from alien import Alien



class AlienInvasion:
     """Overall class to manage game assets and behavior."""
     def __init__(self):
          """Intializing game and creating game resources"""
          pygame.init()
          self.clock = pygame.time.Clock()
          self.setting = Setting()

        #   self.screen = pygame.display.set_mode(
        #       (self.setting.screen_width, self.setting.screen_height))
          
          self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
          self.settings.screen_width = self.screen.get_rect().width
          self.settings.screen_height = self.screen.get_rect().height
          pygame.display.set_caption("Alien Invasion")

          # instance of gamestats
          self.stats = GameStats(self)

          self.ship = Ship(self)
          self.bullets = pygame.sprite.Group()
          self.alien = pygame.sprite.Group()

          self._create_fleet()

          # Start alien invasion in an active stat
          self.game_active = True

          # Start alien invasion in an inactive state
          self.game_active = False

          # make the play button
          self.play_button = Button(self, "Play")

     def _create_fleet(self):
          """Create the fleet of aliens"""
        #   spacing between alien is one alien width and one alien hieght
        #   make an alien
          alien = Alien(self)
          alien_width, alien_height = alien.rect.size

          current_x, current_y = alien_width, alien_height
          while current_y < (self.setting.screen_height - 3 * alien_height):
            while current_x < (self.setting.screen_width - 2 * alien_width):
               self._create_alien(current_x, current_y)
               current_x += 2 * alien_width 

            # finished a row; reset x value increament y value
            current_x = alien_width
            current_y += 2 * alien_height

     def _create_alien(self, x_position, y_position):
               """Create alien and place it in the fleet"""
               new_alien = Alien(self)
               new_alien.x = x_position
               new_alien.rect.x = x_position
               new_alien.rect.y = y_position
               self.aliens.add(new_alien)

     def _ship_hit(self):
          """Respond to ship being hit"""
          if self.stats.ships_left > 0:  
               # decrement ship_left.
               self.stats.ships_left -= 1

               # get rid of any remaining bullets and aliens
               self.bullets.empty()
               self.alien.empty()

               # Create a new fleet and center the ship
               self._create_fleet()
               self.ship.center_ship()

               # puase
               sleep (0.5)
          else:
               self.game_active = False

     def _check_fleet_edges(self):
          """Respond appropriately if any alien have reached an edge"""
          for alien in self.aliens.sprites():
               if alien.check_edges():
                    self._change_fleet_direction()
                    break
                    
     def _change_fleet_direction(self):
          """drop the entire fleet and change the fleet direction"""
          for alien in self.alien.sprites():
               alien.rect.y += self.setting.fleet_drop_speed
          self.settings.fleet_direction *= -1               

     def run_game(self):
          """Start the main loop for the game"""
          while True:
            
            self._check_events()
            if self.game_active:
               self.ship.update()
               self._update_bullets()
               self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

            print(len(self.bullets))

            # set the background color
            # self.bg_color = (230, 230, 230)

     def _update_bullets(self):
             """update the position of the bullets, get rid of old bullets"""
             # update bullet positions.  
             self.bullets.update()

            # get rid of bullets that have disapeared
             for bullet in self.bullets.copy():
                 if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)

             self._check_bullet_alien_collision()

     def _check_bullet_alien_collision(self):
            """Respond to bullet-alien collision"""
            #   remove any bullet and alien that have colided
            collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True
             )
            if not self.aliens:
                    #   Destroy existing bullets and create new fleet
                 self.bullets.empty()
                 self._create_fleet()
        

     def _update_aliens(self):
          """Check if the fleet is at an edge then Update positions."""
          self._check_fleet_edges()
          self.aliens.update()

        #   look for alien-ship colission 
          if pygame.sprite.spritecollideany(self.ship, self.aliens):
               self._ship_hit()

          # look if alien hit the bottom of screen
          self._check_aliens_bottom()

     def _check_events(self):
         """respond to keypresses and mouse events."""
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                  self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos
                     self._check_play_button(mouse_pos)

     def _check_play_button(self, mouse_pos):
          """Start the new game when player click play"""
          if self.play_button.rect.collidepoint(mouse_pos):
               self.game_active = True

     def _check_keydown_events(self, event):
        #    respond to keypresses
            if event.key == pygame.K_RIGHT:
                 self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                 sys.exit()
            elif event.key == pygame.K_SPACE:
                 self._fire_bullet()
     def _check_keyup_events(self, event):
        #   respond to keypresses
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
     def _fire_bullet(self):
            """create new bullets and add it to screen"""
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullets = Bullet(self)
                self.bullets.add(new_bullets)


     def _update_screen(self):
            """update images on the screen and flip to new screen"""
            self.screen.fill(self.setting.bg_color)
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

          #   drawing the play button
            if not self.game_active:
                 self.play_button.draw_button()

            pygame.display.flip()

     def _check_aliens_bottom(self):
          """check if aliens have reached the bottom of the screen"""
          for alien in self.aliens.sprties():
               if alien.rect.bottom >= self.screen.screen_height:
                    # treat this the same as if ship got hit
                    self._ship_hit()
                    break

if __name__ == '__main__':
    # Make game instance, and rub the game
    ai = AlienInvasion()
    ai.run_game
    