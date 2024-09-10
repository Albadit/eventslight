// database seed: npx prisma db seed
// database reset and seed: npx prisma db push --force-reset && npx prisma db seed
// prisma prefix: npx prisma

import { PrismaClient } from "@prisma/client";

const db = new PrismaClient();

async function main() {
  console.log('Seed data created successfully');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await db.$disconnect();
  });
