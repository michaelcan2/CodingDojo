﻿// <auto-generated />
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage;
using Microsoft.EntityFrameworkCore.Storage.Internal;
using System;
using WeddingPlanner.Models;

namespace WeddingPlanner.Migrations
{
    [DbContext(typeof(WeddingPlannerContext))]
    [Migration("20180521193253_FirstMigration")]
    partial class FirstMigration
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn)
                .HasAnnotation("ProductVersion", "2.0.3-rtm-10026");

            modelBuilder.Entity("WeddingPlanner.Models.RSVP", b =>
                {
                    b.Property<int>("id")
                        .ValueGeneratedOnAdd();

                    b.Property<DateTime>("created_at");

                    b.Property<DateTime>("updated_at");

                    b.Property<int?>("userid");

                    b.Property<int?>("weddingid");

                    b.HasKey("id");

                    b.HasIndex("userid");

                    b.HasIndex("weddingid");

                    b.ToTable("RSVP");
                });

            modelBuilder.Entity("WeddingPlanner.Models.User", b =>
                {
                    b.Property<int>("id")
                        .ValueGeneratedOnAdd();

                    b.Property<DateTime>("created_at");

                    b.Property<string>("email");

                    b.Property<string>("first_name");

                    b.Property<string>("last_name");

                    b.Property<string>("password");

                    b.Property<DateTime>("updated_at");

                    b.HasKey("id");

                    b.ToTable("Users");
                });

            modelBuilder.Entity("WeddingPlanner.Models.Wedding", b =>
                {
                    b.Property<int>("id")
                        .ValueGeneratedOnAdd();

                    b.Property<string>("address");

                    b.Property<DateTime>("created_at");

                    b.Property<DateTime?>("date");

                    b.Property<DateTime>("updated_at");

                    b.Property<int?>("userid");

                    b.Property<string>("wedderone");

                    b.Property<string>("weddertwo");

                    b.HasKey("id");

                    b.HasIndex("userid");

                    b.ToTable("Wedding");
                });

            modelBuilder.Entity("WeddingPlanner.Models.RSVP", b =>
                {
                    b.HasOne("WeddingPlanner.Models.User", "user")
                        .WithMany("weddings")
                        .HasForeignKey("userid");

                    b.HasOne("WeddingPlanner.Models.Wedding", "wedding")
                        .WithMany("attendees")
                        .HasForeignKey("weddingid");
                });

            modelBuilder.Entity("WeddingPlanner.Models.Wedding", b =>
                {
                    b.HasOne("WeddingPlanner.Models.User", "creator")
                        .WithMany()
                        .HasForeignKey("userid");
                });
#pragma warning restore 612, 618
        }
    }
}
